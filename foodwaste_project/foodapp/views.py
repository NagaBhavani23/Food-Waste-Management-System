from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
import math
from .models import Donation, DonorProfile, NGOProfile, FoodRequest
from .forms import DonationForm

# Haversine formula to calculate distance between two coordinates
def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate distance in kilometers between two lat/long coordinates."""
    R = 6371  # Earth's radius in kilometers
    
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    
    a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    distance = R * c
    
    return round(distance, 2)

# Home Page View
def home(request):
    donations = Donation.objects.filter(status='Pending').order_by('-created_at')[:9]
    total_donations = Donation.objects.count()
    total_requests = FoodRequest.objects.count()
    
    context = {
        'donations': donations,
        'total_donations': total_donations,
        'total_requests': total_requests,
    }
    return render(request, 'home.html', context)

# User Registration View
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')
        
        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                
                # Create profile based on user type
                if user_type == 'donor':
                    DonorProfile.objects.create(user=user)
                    messages.success(request, 'Donor account created successfully! Please login.')
                elif user_type == 'ngo':
                    NGOProfile.objects.create(
                        user=user,
                        organization_name=request.POST.get('org_name', ''),
                        registration_number=request.POST.get('reg_number', ''),
                        phone=request.POST.get('phone', ''),
                        address=request.POST.get('address', ''),
                        city=request.POST.get('city', '')
                    )
                    messages.success(request, 'NGO account created successfully! Please login.')
                
                return redirect('login')
            else:
                messages.error(request, 'Username already exists!')
        else:
            messages.error(request, 'Passwords do not match!')
    
    return render(request, 'register.html')

# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')
    
    return render(request, 'login.html')

# User Logout View
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')

# Dashboard View
@login_required(login_url='login')
def dashboard(request):
    user = request.user
    
    # Check if user is a donor or NGO
    is_donor = DonorProfile.objects.filter(user=user).exists()
    is_ngo = NGOProfile.objects.filter(user=user).exists()
    
    context = {
        'is_donor': is_donor,
        'is_ngo': is_ngo,
    }
    
    # Show all donations on dashboard for visibility
    donations = Donation.objects.all().order_by('-created_at')
    context['donations'] = donations

    if is_donor:
        # donor-specific stats
        my_donations = donations.filter(donor=user)
        context['my_donations'] = my_donations
        context['total_donations'] = my_donations.count()

    if is_ngo:
        food_requests = FoodRequest.objects.filter(ngo=user)
        context['food_requests'] = food_requests
        context['total_requests'] = food_requests.count()
    
    return render(request, 'dashboard.html', context)

# Donate Food View
@login_required(login_url='login')
def donate_food(request):
    # Check if user is a donor
    if not DonorProfile.objects.filter(user=request.user).exists():
        messages.error(request, 'Only donors can create donations!')
        return redirect('dashboard')
    
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        location = request.POST.get('location')
        contact_number = request.POST.get('contact_number')
        
        donation = Donation.objects.create(
            donor=request.user,
            food_name=food_name,
            description=description,
            quantity=quantity,
            location=location,
            contact_number=contact_number
        )
        
        messages.success(request, 'Donation created successfully!')
        return redirect('dashboard')
    
    return render(request, 'donate.html')


@login_required(login_url='login')
def add_donation(request):
    # Only donors can add donations
    if not DonorProfile.objects.filter(user=request.user).exists():
        messages.error(request, 'Only donors can add donations!')
        return redirect('dashboard')

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user
            donation.status = 'Pending'
            # Handle latitude and longitude
            try:
                if form.cleaned_data.get('latitude'):
                    donation.latitude = form.cleaned_data['latitude']
                if form.cleaned_data.get('longitude'):
                    donation.longitude = form.cleaned_data['longitude']
            except (ValueError, KeyError):
                pass
            donation.save()
            messages.success(request, 'Donation added successfully!')
            return redirect('dashboard')
    else:
        form = DonationForm()

    return render(request, 'add_donation.html', {'form': form})

# Request Food View
@login_required(login_url='login')
def request_food(request):
    # Check if user is an NGO
    if not NGOProfile.objects.filter(user=request.user).exists():
        messages.error(request, 'Only NGOs can request food!')
        return redirect('dashboard')
    
    if request.method == 'POST':
        food_type = request.POST.get('food_type')
        quantity_needed = request.POST.get('quantity_needed')
        location = request.POST.get('location')
        contact_number = request.POST.get('contact_number')
        notes = request.POST.get('notes')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
        # Convert to float if provided
        lat = float(latitude) if latitude else None
        lon = float(longitude) if longitude else None
        
        food_request = FoodRequest.objects.create(
            ngo=request.user,
            food_type=food_type,
            quantity_needed=quantity_needed,
            location=location,
            contact_number=contact_number,
            notes=notes,
            latitude=lat,
            longitude=lon
        )
        
        messages.success(request, 'Food request submitted successfully!')
        return redirect('dashboard')
    
    available_donations = Donation.objects.filter(status='Pending')
    context = {'available_donations': available_donations}
    return render(request, 'request.html', context)

# View All Donations
def view_donations(request):
    donations = Donation.objects.filter(status='Pending')
    
    # Search functionality
    search = request.GET.get('search')
    if search:
        donations = donations.filter(
            Q(food_name__icontains=search) | 
            Q(location__icontains=search)
        )
    
    context = {'donations': donations, 'search': search}
    return render(request, 'all_donations.html', context)

# View Donation Detail
def donation_detail(request, id):
    donation = get_object_or_404(Donation, id=id)
    requests = FoodRequest.objects.filter(donation=donation)
    
    context = {
        'donation': donation,
        'requests': requests,
    }
    return render(request, 'donation_detail.html', context)

# Claim Donation
@login_required(login_url='login')
def claim_donation(request, id):
    donation = get_object_or_404(Donation, id=id)

    # Only receivers (NGO) can claim
    if not NGOProfile.objects.filter(user=request.user).exists():
        messages.error(request, 'Only receivers can claim donations!')
        return redirect('dashboard')

    if donation.status != 'Pending':
        messages.warning(request, 'Donation cannot be claimed.')
        return redirect('dashboard')

    donation.status = 'Claimed'
    donation.claimed_by = request.user
    donation.save()

    messages.success(request, 'Donation claimed — awaiting donor acceptance.')
    return redirect('dashboard')


@login_required(login_url='login')
def accept_donation(request, id):
    donation = get_object_or_404(Donation, id=id)

    # Only the donor who created the donation can accept
    if donation.donor != request.user:
        messages.error(request, 'Only the donor can accept this claim.')
        return redirect('dashboard')

    if donation.status != 'Claimed':
        messages.warning(request, 'Donation is not in a claimed state.')
        return redirect('dashboard')

    donation.status = 'Accepted'
    donation.save()
    messages.success(request, 'Donation claim accepted.')
    return redirect('dashboard')

# NGO Accept Claimed Donation
@login_required(login_url='login')
def ngo_accept_donation(request, id):
    donation = get_object_or_404(Donation, id=id)
    
    # Only the NGO that claimed it can accept
    if donation.claimed_by != request.user:
        messages.error(request, 'Only the NGO that claimed this donation can accept it.')
        return redirect('receiver_dashboard')
    
    if donation.status not in ['Claimed', 'Accepted']:
        messages.warning(request, 'This donation cannot be accepted.')
        return redirect('receiver_dashboard')
    
    donation.status = 'Accepted'
    donation.save()
    messages.success(request, 'Donation accepted successfully!')
    return redirect('receiver_dashboard')

# NGO Reject Claimed Donation
@login_required(login_url='login')
def ngo_reject_donation(request, id):
    donation = get_object_or_404(Donation, id=id)
    
    # Only the NGO that claimed it can reject
    if donation.claimed_by != request.user:
        messages.error(request, 'Only the NGO that claimed this donation can reject it.')
        return redirect('receiver_dashboard')
    
    if donation.status != 'Claimed':
        messages.warning(request, 'This donation cannot be rejected.')
        return redirect('receiver_dashboard')
    
    donation.status = 'Pending'
    donation.claimed_by = None
    donation.save()
    messages.success(request, 'Donation claim rejected. It is now available for other NGOs.')
    return redirect('receiver_dashboard')

# Receiver Dashboard View (NGO)
@login_required(login_url='login')
def receiver_dashboard(request):
    # Check if user is an NGO
    if not NGOProfile.objects.filter(user=request.user).exists():
        messages.error(request, 'This page is for NGOs only!')
        return redirect('dashboard')
    
    # Get all available donations (Pending only)
    available_donations = Donation.objects.filter(status='Pending').order_by('-created_at')
    
    # Get donations claimed by this NGO
    claimed_donations = Donation.objects.filter(
        claimed_by=request.user
    ).exclude(status='Pending').order_by('-created_at')
    
    # Get all food requests from this NGO
    my_requests = FoodRequest.objects.filter(ngo=request.user).order_by('-requested_at')
    
    # Sync food request statuses with donation statuses
    for food_request in my_requests:
        if food_request.donation:
            if food_request.donation.status == 'Pending':
                if food_request.status != 'pending':
                    food_request.status = 'pending'
                    food_request.save()
            elif food_request.donation.status == 'Claimed':
                if food_request.status != 'pending':
                    food_request.status = 'pending'
                    food_request.save()
            elif food_request.donation.status == 'Accepted':
                if food_request.status != 'approved':
                    food_request.status = 'approved'
                    food_request.save()
            elif food_request.donation.status == 'Completed':
                if food_request.status != 'completed':
                    food_request.status = 'completed'
                    food_request.save()
    
    # Refresh requests after sync
    my_requests = FoodRequest.objects.filter(ngo=request.user).order_by('-requested_at')
    
    # Statistics
    total_donations_available = available_donations.count()
    total_requests = my_requests.count()
    pending_requests = my_requests.filter(status='pending').count()
    approved_requests = my_requests.filter(status='approved').count()
    
    context = {
        'donations': available_donations,
        'claimed_donations': claimed_donations,
        'requests': my_requests,
        'total_donations_available': total_donations_available,
        'total_requests': total_requests,
        'pending_requests': pending_requests,
        'approved_requests': approved_requests,
    }
    
    return render(request, 'receiver_dashboard.html', context)

# Send Food Request from Receiver Dashboard
@login_required(login_url='login')
def send_request(request, donation_id):
    # Check if user is an NGO
    if not NGOProfile.objects.filter(user=request.user).exists():
        messages.error(request, 'Only NGOs can send food requests!')
        return redirect('home')
    
    donation = get_object_or_404(Donation, id=donation_id)
    
    # Check if NGO already has a pending request for this donation
    existing_request = FoodRequest.objects.filter(
        ngo=request.user,
        donation=donation,
        status='pending'
    ).exists()
    
    if existing_request:
        messages.warning(request, 'You already have a pending request for this donation!')
        return redirect('receiver_dashboard')
    
    # Create a food request
    food_request = FoodRequest.objects.create(
        ngo=request.user,
        donation=donation,
        food_type=donation.food_name,
        quantity_needed=donation.quantity,
        location=donation.location,
        status='pending'
    )
    
    messages.success(request, f'Request sent for {donation.food_name}! Waiting for donor approval.')
    return redirect('receiver_dashboard')
