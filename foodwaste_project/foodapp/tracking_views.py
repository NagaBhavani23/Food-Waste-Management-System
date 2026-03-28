"""Location tracking views for food donations."""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Donation, FoodRequest
import json
import math


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


@login_required(login_url='login')
def track_request(request, request_id):
    """Display map with donor and receiver locations for a food request."""
    food_request = get_object_or_404(FoodRequest, id=request_id)
    donation = food_request.donation
    
    # Check authorization: only NGO who made request or donor can view
    is_authorized = (request.user == food_request.ngo or request.user == donation.donor)
    if not is_authorized:
        from django.contrib import messages
        messages.error(request, 'You are not authorized to view this tracking.')
        return redirect('dashboard')
    
    # Calculate distance if both locations available
    distance = None
    if (donation.latitude and donation.longitude and 
        food_request.latitude and food_request.longitude):
        distance = haversine_distance(
            donation.latitude, donation.longitude,
            food_request.latitude, food_request.longitude
        )
    
    context = {
        'food_request': food_request,
        'donation': donation,
        'distance': distance,
        'donor_name': donation.donor.username,
        'ngo_name': food_request.ngo.username,
    }
    return render(request, 'track_request.html', context)


@login_required(login_url='login')
@require_http_methods(["POST"])
def save_location(request):
    """AJAX endpoint to save user's current GPS location."""
    try:
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        location_type = data.get('type')  # 'donation' or 'request'
        object_id = data.get('id')
        
        if location_type == 'donation':
            donation = get_object_or_404(Donation, id=object_id, donor=request.user)
            donation.latitude = latitude
            donation.longitude = longitude
            donation.save()
            return JsonResponse({'status': 'success', 'message': 'Donor location saved'})
        
        elif location_type == 'request':
            food_request = get_object_or_404(FoodRequest, id=object_id, ngo=request.user)
            food_request.latitude = latitude
            food_request.longitude = longitude
            food_request.save()
            return JsonResponse({'status': 'success', 'message': 'Receiver location saved'})
        
        return JsonResponse({'status': 'error', 'message': 'Invalid location type'}, status=400)
    
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@login_required(login_url='login')
def get_location_data(request, request_id):
    """AJAX endpoint to get current location data of donor and receiver."""
    food_request = get_object_or_404(FoodRequest, id=request_id)
    donation = food_request.donation
    
    # Check authorization
    is_authorized = (request.user == food_request.ngo or request.user == donation.donor)
    if not is_authorized:
        return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)
    
    # Calculate distance if both locations available
    distance = None
    if (donation.latitude and donation.longitude and 
        food_request.latitude and food_request.longitude):
        distance = haversine_distance(
            donation.latitude, donation.longitude,
            food_request.latitude, food_request.longitude
        )
    
    data = {
        'donor': {
            'name': donation.donor.username,
            'location': donation.location,
            'latitude': donation.latitude,
            'longitude': donation.longitude,
        },
        'receiver': {
            'name': food_request.ngo.username,
            'location': food_request.location,
            'latitude': food_request.latitude,
            'longitude': food_request.longitude,
        },
        'distance': distance,
        'status': food_request.status,
    }
    return JsonResponse(data)
