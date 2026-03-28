# Quick Start Guide - FeedForward

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

## Step-by-Step Setup

### 1. Navigate to Project Directory
```bash
cd "d:\Next gen 4.o\day 16 project\foodwaste_project"
```

### 2. Activate Virtual Environment (if needed)
```bash
# Windows
env\Scripts\activate

# Mac/Linux
source env/bin/activate
```

### 3. Install Dependencies (Optional - Dependencies should already be installed)
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations (if you reset the database)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a New Superuser Account (Optional)
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### 7. Access the Application
- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
  - Username: `admin`
  - Password: `admin123`

## Default Test Account

**Admin Credentials:**
- Username: `admin`
- Password: `admin123`
- Access: http://127.0.0.1:8000/admin/

## Main Pages

### Public Pages
- **Home** (`/`): Landing page with featured donations
- **View All Donations** (`/donations/`): Browse all available donations
- **Login** (`/login/`): User login page
- **Register** (`/register/`): User registration page

### Authenticated Pages (Requires Login)
- **Dashboard** (`/dashboard/`): User's personal dashboard
- **Donate Food** (`/donate/`): Create a new food donation
- **Request Food** (`/request-food/`): Submit food request (for NGOs)
- **Donation Detail** (`/donations/<id>/`): View full donation details
- **Claim Donation** (`/claim/<id>/`): Claim a specific donation

### Admin Pages
- **Admin Panel** (`/admin/`): Django admin interface
- Manage Users
- Manage Donations
- Manage Food Requests
- Manage Donor Profiles
- Manage NGO Profiles

## Testing the System

### Test as a Donor
1. Go to http://127.0.0.1:8000/register/
2. Choose "Donor" as account type
3. Fill in the form and submit
4. Login with your new account
5. Click "Donate Food" and create a donation
6. View your donations in the dashboard

### Test as an NGO
1. Go to http://127.0.0.1:8000/register/
2. Choose "NGO" as account type
3. Fill in organization details
4. Login with your new account
5. Click "Request Food" to submit a request
6. Browse and claim available donations

### Test Admin Features
1. Go to http://127.0.0.1:8000/admin/
2. Login with admin credentials
3. Manage all users, donations, and requests
4. Update donation and request statuses

## File Structure Overview

```
foodwaste_project/
├── manage.py                    # Django management script
├── db.sqlite3                  # SQLite database
├── requirements.txt            # Python dependencies
├── README.md                   # Full documentation
├── QUICKSTART.md              # This file
│
├── foodwaste_project/          # Project settings
│   ├── settings.py             # Django configuration
│   ├── urls.py                 # URL routing
│   └── wsgi.py                 # WSGI config
│
├── foodapp/                    # Main application
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # App URL patterns
│   ├── admin.py                # Admin interface
│   └── migrations/             # Database migrations
│
├── templates/                  # HTML templates
│   ├── base.html               # Base template
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── donate.html
│   ├── request.html
│   ├── all_donations.html
│   └── donation_detail.html
│
└── static/                     # Static files
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Common Commands

```bash
# Run the server
python manage.py runserver

# Run on specific port
python manage.py runserver 8001

# Create migrations for model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create a superuser account
python manage.py createsuperuser

# Reset all migrations (be careful!)
python manage.py flush

# Open Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic --noinput
```

## Troubleshooting

### Q: Port 8000 is already in use
A: Use a different port: `python manage.py runserver 8001`

### Q: Getting TemplateDoesNotExist error
A: Make sure you're in the `foodwaste_project` directory where `manage.py` is located

### Q: Database locked error
A: Delete `db.sqlite3` and rerun migrations:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Q: Static files not showing
A: Run: `python manage.py collectstatic`

### Q: Can't login with any account
A: Reset admin password:
```bash
python manage.py changepassword admin
```

## Features to Try

1. ✅ Register as Donor and create food donations
2. ✅ Register as NGO and request food
3. ✅ Search and filter donations
4. ✅ Claim donations as an NGO
5. ✅ View donation details
6. ✅ Manage your profile and donations in dashboard
7. ✅ Admin panel to manage all users and donations
8. ✅ View donation requests
9. ✅ Responsive mobile design
10. ✅ Form validation and error messages

## Next Steps

After testing the basic functionality:

1. **Explore the Code**: Review the views, models, and templates
2. **Modify Styling**: Edit `static/css/style.css` to customize colors
3. **Add Features**: Extend models and views with new functionality
4. **Deploy**: Prepare for production deployment

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/en/6.0/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [HTML/CSS Reference](https://developer.mozilla.org/en-US/docs/Web/Guide)
- [JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## Support

If you encounter any issues:
1. Check the terminal output for error messages
2. Verify all files are in the correct locations
3. Make sure the virtual environment is activated
4. Check database migrations are applied
5. Clear browser cache (Ctrl+Shift+Delete)

---

**Ready to start?** Run `python manage.py runserver` and visit http://127.0.0.1:8000/
