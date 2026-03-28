from django.contrib import admin
from .models import DonorProfile, NGOProfile, Donation, FoodRequest

# Donor Profile Admin
class DonorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'created_at')
    list_filter = ('created_at', 'city')
    search_fields = ('user__username', 'phone', 'city')
    
admin.site.register(DonorProfile, DonorProfileAdmin)

# NGO Profile Admin
class NGOProfileAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'registration_number', 'city', 'created_at')
    list_filter = ('created_at', 'city')
    search_fields = ('organization_name', 'registration_number', 'city')
    
admin.site.register(NGOProfile, NGOProfileAdmin)

# Donation Admin
class DonationAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'donor', 'quantity', 'location', 'contact_number', 'status', 'claimed_by', 'created_at')
    list_filter = ('status', 'created_at', 'location')
    search_fields = ('food_name', 'donor__username', 'location', 'contact_number', 'claimed_by__username')
    readonly_fields = ('created_at',)
    
admin.site.register(Donation, DonationAdmin)

# Food Request Admin
class FoodRequestAdmin(admin.ModelAdmin):
    list_display = ('food_type', 'ngo', 'status', 'quantity_needed', 'location', 'contact_number', 'requested_at')
    list_filter = ('status', 'requested_at', 'location')
    search_fields = ('food_type', 'ngo__username', 'location', 'contact_number')
    readonly_fields = ('requested_at', 'updated_at')
    
admin.site.register(FoodRequest, FoodRequestAdmin)
