from django import forms
from .models import Donation, FoodRequest


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['food_name', 'quantity', 'location', 'contact_number', 'description']
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Rice, Vegetables'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 5 kg, 10 servings'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Main Street, Downtown'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 98765 43210', 'type': 'tel'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any additional details about the food...'}),
        }


class FoodRequestForm(forms.ModelForm):
    class Meta:
        model = FoodRequest
        fields = ['food_type', 'quantity_needed', 'location', 'contact_number', 'notes']
        widgets = {
            'food_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Rice, Vegetables, Cooked Meals'}),
            'quantity_needed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 10 kg, 20 servings'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Delivery location'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 98765 43210', 'type': 'tel'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Special requirements or preferences...'}),
        }
