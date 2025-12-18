# Movie Ticket Booking System

A backend-focused web application for booking movie tickets, built using **Django** and **Django REST Framework (DRF)**.  
The project exposes secure REST APIs that can be consumed by web or mobile frontends.

---

## Features

- User registration and login using **JWT authentication**
- Browse available movies and show details
- Book movie tickets securely
- Admin panel to manage movies and bookings
- RESTful API design for frontend/mobile integration
- Interactive API documentation using **Swagger (drf-yasg)**

---

## Tech Stack

- **Backend:** Python, Django, Django REST Framework  
- **Authentication:** JWT (djangorestframework-simplejwt)  
- **Database:** SQLite (can be replaced with PostgreSQL/MySQL)  
- **API Docs:** Swagger (drf-yasg)

---

## Project Structure

movie-ticket-booking-system/
├── backend/
├── booking/
├── manage.py
├── serializers.py
├── models.py
├── views.py
├── urls.py
└── README.md


---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Mudi-Srilakshmi/movie-ticket-booking-system.git
cd movie-ticket-booking-system
```

### 2. Create and activate virtual environment
```bash
python -m venv env
source env/Scripts/activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server
```bash
python manage.py runserver
```

---

## API Endpoints

POST /api/signup/ – User registration
POST /api/login/ – User login (JWT)
GET /api/movies/ – List all movies
POST /api/book/ – Book a ticket

---

## API Documentation

Swagger UI available at:

http://127.0.0.1:8000/swagger/

---

## Future Improvements

Seat selection and availability logic
Payment gateway integration
Booking history for users
Deployment using Docker and cloud platforms

---

## Author

Srilakshmi Mudi
Aspiring Python & Django Developer
