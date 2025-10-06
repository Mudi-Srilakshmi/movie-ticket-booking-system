from django.urls import path
from .views import (
    SignupView,
    MovieListView,
    ShowListView,
    BookSeatView,
    CancelBookingView,
    MyBookingsView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # -----------------------------
    # Authentication endpoints
    # -----------------------------
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh

    # -----------------------------
    # Movie and show endpoints
    # -----------------------------
    path('movies/', MovieListView.as_view(), name='movies_list'),
    path('movies/<int:id>/shows/', ShowListView.as_view(), name='movie_shows'),

    # -----------------------------
    # Booking endpoints
    # -----------------------------
    path('shows/<int:id>/book/', BookSeatView.as_view(), name='book_seat'),
    path('bookings/<int:id>/cancel/', CancelBookingView.as_view(), name='cancel_booking'),
    path('my-bookings/', MyBookingsView.as_view(), name='my_bookings'),
]
