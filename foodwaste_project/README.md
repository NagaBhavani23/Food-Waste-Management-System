# FeedForward

## Project Overview

A comprehensive web-based FeedForward platform built with Django that connects food donors with NGOs to reduce food waste and help communities in need.

## Features

### User Management
- **User Registration**: Support for Donor and NGO account creation
- **User Authentication**: Secure login and logout functionality
- **Profile Management**: Separate profiles for donors and NGOs with organization details

### Donor Features
- **Create Donations**: Post food donations with details (food name, quantity, location, description)
- **Manage Donations**: View and manage all posted donations
- **Track Requests**: See which NGOs have requested their donations
- **Donation Status**: Track donation status (Available, Claimed, Expired, Completed)

### NGO Features
- **Request Food**: Submit food requests with specific needs
- **Browse Donations**: View all available donations
- **Claim Donations**: Claim specific donations matching their needs
- **Manage Requests**: Track all submitted food requests and their status

### Admin Features
- **User Management**: Manage all user accounts
- **Donation Management**: Monitor and manage all donations
- **Request Management**: Handle food requests and approve/reject them
- **Profile Management**: Manage donor and NGO profiles
- **Analytics Dashboard**: View system statistics

## Project Structure

```
foodwaste_project/
├── foodwaste_project/          # Main project folder
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── manage.py               # Management script
├── foodapp/                    # Main Django app
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # App URL routing
│   ├── admin.py                # Admin configuration
│   └── migrations/             # Database migrations
├── templates/                  # HTML templates
│   ├── base.html               # Base template
│   ├── home.html               # Home page
│   ├── register.html           # Registration page
│   ├── login.html              # Login page
│   ├── dashboard.html          # User dashboard
│   ├── donate.html             # Donation form
│   ├── request.html            # Food request form
│   ├── all_donations.html      # View all donations
│   └── donation_detail.html    # Donation details page
├── static/                     # Static files
│   ├── css/
│   │   └── style.css           # Global styles
│   └── js/
│       └── script.js           # Client-side functionality
└── db.sqlite3                  # SQLite database
```

## Database Models

### 1. User (Django built-in)
- Standard Django User model for authentication

### 2. DonorProfile
- One-to-One relationship with User
- Stores donor contact information

### 3. NGOProfile
- One-to-One relationship with User
- Stores organization details and registration information

### 4. Donation
- Links donor with their food donations
- Tracks status (Available, Claimed, Expired, Completed)
- Stores food details, location, and contact information

### 5. FoodRequest
- Links NGO with their food requests
- Can be linked to specific donations
- Tracks request status (Pending, Approved, Rejected, Completed)

## Installation & Setup

### Step 1: Set up Python Environment
```bash
python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # Mac/Linux
```

### Step 2: Install Django
```bash
pip install django
```

### Step 3: Create Django Project
```bash
django-admin startproject foodwaste_project
cd foodwaste_project
```

### Step 4: Create Django App
```bash
python manage.py startapp foodapp
```

### Step 5: Configure Settings
- Add 'foodapp' to INSTALLED_APPS in settings.py
- Configure TEMPLATES directory
- Configure STATIC files

### Step 6: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create Superuser
```bash
python manage.py createsuperuser
# Username: admin
# Password: admin123
```

### Step 8: Run Server
```bash
python manage.py runserver
```

Access the application at: http://127.0.0.1:8000/

## Usage Guide

### For Donors

1. **Register**: Create an account as a Donor
2. **Login**: Sign in with your credentials
3. **Donate Food**:
   - Click "Donate Food" button
   - Fill in food details (name, quantity, location, contact)
   - Submit the donation
4. **Track Donations**: View all your donations in the dashboard
5. **Manage Requests**: See which NGOs have requested your food

### For NGOs

1. **Register**: Create an organization account
2. **Login**: Sign in with your credentials
3. **Request Food**:
   - Click "Request Food" button
   - Specify food type and quantity needed
   - Submit request
4. **Claim Donations**: Browse available donations and claim matching ones
5. **Track Requests**: Monitor all your food requests in the dashboard

### For Admin

1. **Access Admin Panel**: Go to http://127.0.0.1:8000/admin/
2. **Login**: Use superuser credentials (admin/admin123)
3. **Manage Users**: Add, edit, or delete user accounts
4. **Manage Donations**: Review and modify donation details
5. **Manage Requests**: Approve or reject food requests
6. **Manage Profiles**: View and manage donor and NGO profiles

## Features Implemented

### Core Functionality
- ✅ User Registration (Donor & NGO)
- ✅ User Authentication (Login/Logout)
- ✅ Create & Post Donations
- ✅ Request Food
- ✅ Claim Donations
- ✅ View All Donations
- ✅ Search Donations
- ✅ User Dashboard
- ✅ Admin Panel
- ✅ Profile Management

### Frontend
- ✅ Responsive Design
- ✅ Navigation Bar
- ✅ Alert Messages
- ✅ Form Validation
- ✅ Search Functionality
- ✅ Status Badges
- ✅ Data Tables
- ✅ Mobile Friendly

### Backend
- ✅ Django Models
- ✅ Views & URL Routing
- ✅ Database Migrations
- ✅ Admin Interface
- ✅ User Authentication
- ✅ Filtering & Search

## Technology Stack

- **Backend**: Django 6.0.2
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Server**: Django Development Server (for testing)

## Key Template Variables

### Home Page
- `donations`: Recent available donations
- `total_donations`: Total donation count
- `total_requests`: Total request count

### Dashboard
- `is_donor`: Boolean to show donor section
- `is_ngo`: Boolean to show NGO section
- `donations`: User's donations (if donor)
- `food_requests`: User's requests (if NGO)

### All Donations
- `donations`: Filtered donation list
- `search`: Search query term

## CSS Classes & Styling

- `.btn`: Standard button styling
- `.btn-primary`: Green primary action button
- `.btn-secondary`: Blue secondary action button
- `.donation-card`: Card for displaying donations
- `.status-badge`: Status indicator badge
- `.form-group`: Form field container
- `.dashboard-section`: Dashboard section styling

## JavaScript Functions

- `validateForm()`: Form validation
- `confirmDelete()`: Delete confirmation
- `validateEmail()`: Email validation
- `validatePhoneNumber()`: Phone validation
- `formatPhoneNumber()`: Format phone numbers
- `liveTableSearch()`: Real-time table search
- `paginateTable()`: Table pagination

## Admin Features

### Donor Profile Admin
- List: Username, Phone, City, Created Date
- Filter by: Created Date, City
- Search by: Username, Phone, City

### NGO Profile Admin
- List: Organization Name, Registration Number, City, Created Date
- Filter by: Created Date, City
- Search by: Organization Name, Registration Number, City

### Donation Admin
- List: Food Name, Donor, Quantity, Location, Status, Date
- Filter by: Status, Created Date, Location
- Search by: Food Name, Donor, Location

### Food Request Admin
- List: Food Type, NGO, Status, Quantity, Location, Date
- Filter by: Status, Requested Date, Location
- Search by: Food Type, NGO, Location

## Security Features

- CSRF Protection: All forms have {% csrf_token %}
- Password Hashing: Django's built-in password hashing
- User Authentication: Login required for sensitive operations
- SQL Injection Prevention: Django ORM usage
- XSS Protection: Template auto-escaping

## Performance Optimization

- Database indexing on frequently searched fields
- Pagination support for large datasets
- Static file caching
- Query optimization using select_related/prefetch_related

## Future Enhancements

1. **Email Notifications**: Notify users about requests/claims
2. **Image Upload**: Allow photos of food items
3. **Real-time Chat**: Direct messaging between donors and NGOs
4. **Location Mapping**: Google Maps integration
5. **Mobile App**: React Native or Flutter app
6. **Payment Integration**: For premium features
7. **Review & Rating**: User reviews and ratings
8. **Analytics Dashboard**: Detailed statistics and insights
9. **API Development**: RESTful API for mobile app
10. **Multi-language Support**: Internationalization

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Database Issues
```bash
python manage.py flush  # Reset database
python manage.py makemigrations
python manage.py migrate
```

### Module Import Errors
```bash
pip install -r requirements.txt
```

## Demo Credentials

- **Admin Panel**: 
  - Username: `admin`
  - Password: `admin123`
  - URL: http://127.0.0.1:8000/admin/

## Testing Scenarios

### Donor Workflow
1. Register as donor
2. Post a food donation
3. See requests from NGOs
4. Update donation status

### NGO Workflow
1. Register as NGO
2. Browse available donations
3. Claim a donation
4. Submit food request
5. Check request status

### Admin Workflow
1. Login to admin panel
2. Manage users
3. Approve/reject requests
4. View statistics
5. Manage all donations

## Support & Documentation

For more information about Django:
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Security Documentation](https://docs.djangoproject.com/en/6.0/topics/security/)

## License

This project is open source and available for educational purposes.

## Contributors

Built as a comprehensive learning project implementing Django best practices and web development fundamentals.

---

**Project Status**: ✅ Complete and Functional
**Last Updated**: February 24, 2026
