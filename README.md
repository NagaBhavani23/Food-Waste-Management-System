# Food Waste Management System 🍲

A full-stack web application built with **Django** that connects food donors (hotels, restaurants) with NGOs to reduce food wastage. It provides a platform to list surplus food, track donations, and manage distribution efficiently.

## 🚀 Features

- **User Authentication:** Secure login/signup for Donors, NGOs, and Admins using Django's built-in Auth system.
- **Food Donation Listings:** Donors can create, update, and delete food listings with quantity and expiry details.
- **Real-time Dashboard:** Admins can monitor donation trends and distribution status.
- **Responsive UI:** A clean, mobile-friendly interface built with HTML5, CSS3, and JavaScript.
- **Search & Filter:** Find available food by location or category.

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla/jQuery)
- **Database:** SQLite (Default) or PostgreSQL/MySQL
- **Styling:** Bootstrap (Optional)

## 📥 Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com
cd food-waste-management
Use code with caution.

2. Create a Virtual Environment
bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Use code with caution.

3. Install Dependencies
bash
pip install django
# If you have a requirements file:
pip install -r requirements.txt
Use code with caution.

4. Database Migrations
Apply the initial Django migrations to set up your database schema.
bash
python manage.py makemigrations
python manage.py migrate
Use code with caution.

5. Create a Superuser (Admin)
bash
python manage.py createsuperuser
Use code with caution.

6. Run the Development Server
bash
python manage.py runserver
Use code with caution.

Visit http://127.0.0.1:8000/ in your browser 
