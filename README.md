# Movie Ticket Booking System

A Django-based web application for booking movie tickets, allowing users to browse movies, select showtimes, and book seats. The backend is built using Django and Django REST Framework (DRF).

## Features

- User signup, login, and authentication (JWT)
- Browse movies and showtimes
- Book movie tickets
- Admin panel to manage movies, shows, and bookings
- REST API endpoints for frontend or mobile app integration
- API documentation using Swagger (drf-yasg)

## Tech Stack

- **Backend:** Django, Django REST Framework, djangorestframework-simplejwt, drf-yasg  
- **Database:** SQLite (default, can be replaced with PostgreSQL/MySQL)  
- **Authentication:** JWT  

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mudi-Srilakshmi/movie-ticket-booking-system.git
cd movie-ticket-booking-system

Create a virtual environment:
----------------
python -m venv env
source env/Scripts/activate   # Windows
# or
source env/bin/activate       # macOS/Linux

Install dependencies:
-------------------
pip install -r requirements.txt

Apply migrations:
-----------------
python manage.py makemigrations
python manage.py migrate

Run the development server:
------------------
python manage.py runserver

Open the app in your browser:
------------------
http://127.0.0.1:8000/

API Endpoints
------------------
POST /api/signup/ – Register a new user

POST /api/login/ – Login and get JWT token

GET /api/movies/ – List all movies

POST /api/book/ – Book a ticket

API documentation is available at:
----------------------
http://127.0.0.1:8000/swagger/

Contributing:
-------------
Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m "Add some feature")

Push to the branch (git push origin feature/your-feature)

Create a Pull Request




