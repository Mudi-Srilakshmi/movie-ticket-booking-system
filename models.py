from django.db import models
from django.conf import settings

# -----------------------------
# Movie Model
# -----------------------------
class Movie(models.Model):
    # Title of the movie
    title = models.CharField(max_length=255)
    # Duration of the movie in minutes
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        # For easy identification in admin or shell
        return self.title

# -----------------------------
# Show Model
# -----------------------------
class Show(models.Model):
    # ForeignKey to the Movie model
    movie = models.ForeignKey(Movie, related_name='shows', on_delete=models.CASCADE)
    # Name of the screen where this show is running
    screen_name = models.CharField(max_length=100)
    # Date and time of the show
    date_time = models.DateTimeField()
    # Total number of seats available in this show
    total_seats = models.PositiveIntegerField()

    def __str__(self):
        # Display movie title, screen, and time
        return f"{self.movie.title} @ {self.screen_name} on {self.date_time}"

# -----------------------------
# Booking Model
# -----------------------------
class Booking(models.Model):
    # Booking statuses
    STATUS_BOOKED = 'booked'
    STATUS_CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (STATUS_BOOKED, 'Booked'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    # User who made the booking
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bookings', on_delete=models.CASCADE)
    # The show that was booked
    show = models.ForeignKey(Show, related_name='bookings', on_delete=models.CASCADE)
    # Seat number chosen by the user
    seat_number = models.PositiveIntegerField()
    # Status of the booking (booked or cancelled)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_BOOKED)
    # Timestamp when booking was created
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent double booking of the same seat in the same show
        unique_together = ('show', 'seat_number')
        # Default ordering: newest bookings first
        ordering = ['-created_at']

    def __str__(self):
        # Easy identification of booking
        return f"{self.user} -> {self.show} seat {self.seat_number} ({self.status})"
