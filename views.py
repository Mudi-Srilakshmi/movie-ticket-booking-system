from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Movie, Show, Booking
from .serializers import SignupSerializer, MovieSerializer, ShowSerializer, BookingSerializer

# -----------------------------
# Signup API
# -----------------------------
class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can register

# -----------------------------
# List all movies
# GET /movies/
# -----------------------------
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

# -----------------------------
# List all shows for a movie
# GET /movies/<id>/shows/
# -----------------------------
class ShowListView(generics.ListAPIView):
    serializer_class = ShowSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        movie_id = self.kwargs['id']
        return Show.objects.filter(movie_id=movie_id)

# -----------------------------
# Book a seat
# POST /shows/<id>/book/
# -----------------------------
class BookSeatView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        show = get_object_or_404(Show, id=id)
        seat_number = request.data.get('seat_number')

        # Validate seat_number
        if not seat_number or int(seat_number) < 1 or int(seat_number) > show.total_seats:
            return Response({'error': 'Invalid seat number.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if seat already booked
        if Booking.objects.filter(show=show, seat_number=seat_number, status='booked').exists():
            return Response({'error': 'Seat already booked.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create booking
        booking = Booking.objects.create(
            user=request.user,
            show=show,
            seat_number=seat_number
        )
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# -----------------------------
# Cancel a booking
# POST /bookings/<id>/cancel/
# -----------------------------
class CancelBookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        booking = get_object_or_404(Booking, id=id)

        # Ensure user can cancel only their own booking
        if booking.user != request.user:
            return Response({'error': 'You cannot cancel this booking.'}, status=status.HTTP_403_FORBIDDEN)

        # Cancel the booking
        booking.status = 'cancelled'
        booking.save()
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)

# -----------------------------
# List bookings of logged-in user
# GET /my-bookings/
# -----------------------------
class MyBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
