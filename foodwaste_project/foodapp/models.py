from django.db import models
from django.contrib.auth.models import User

# Donor Profile Model
class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='donor_profile')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - Donor"

# NGO Profile Model
class NGOProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ngo_profile')
    organization_name = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.organization_name} - NGO"

# Donation Model
class Donation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Claimed', 'Claimed'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
    ]

    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    food_name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    claimed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='claimed_donations')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.food_name} by {self.donor.username}"

    class Meta:
        ordering = ['-created_at']

# Food Request Model
class FoodRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]
    
    ngo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_requests')
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, related_name='requests', null=True, blank=True)
    food_type = models.CharField(max_length=200)
    quantity_needed = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requested_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Request for {self.food_type} by {self.ngo.username}"
    
    class Meta:
        ordering = ['-requested_at']
