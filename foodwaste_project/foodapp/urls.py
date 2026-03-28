from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('donate/', views.donate_food, name='donate'),
    path('request-food/', views.request_food, name='request_food'),
    path('donations/', views.view_donations, name='view_donations'),
    path('donations/<int:id>/', views.donation_detail, name='donation_detail'),
    path('claim/<int:id>/', views.claim_donation, name='claim_donation'),
    path('add/', views.add_donation, name='add_donation'),
    path('accept/<int:id>/', views.accept_donation, name='accept_donation'),
    path('ngo-accept/<int:id>/', views.ngo_accept_donation, name='ngo_accept_donation'),
    path('ngo-reject/<int:id>/', views.ngo_reject_donation, name='ngo_reject_donation'),
    path('receiver_dashboard/', views.receiver_dashboard, name='receiver_dashboard'),
    path('send_request/<int:donation_id>/', views.send_request, name='send_request'),
    # Location tracking URLs
]
