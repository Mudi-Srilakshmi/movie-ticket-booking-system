from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Show, Booking

# Get the built-in User model
User = get_user_model()

# -----------------------------
# User Signup Serializer
# -----------------------------
class SignupSerializer(serializers.ModelSerializer):
    # Password should be write-only
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        # Use Django's create_user to hash password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

# -----------------------------
# Movie Serializer
# -----------------------------
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration_minutes']

# -----------------------------
# Show Serializer
# -----------------------------
class ShowSerializer(serializers.ModelSerializer):
    # Include movie title in response (optional)
    movie_title = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = Show
        fields = ['id', 'movie', 'movie_title', 'screen_name', 'date_time', 'total_seats']

# -----------------------------
# Booking Serializer
# -----------------------------
class BookingSerializer(serializers.ModelSerializer):
    # Include related fields for readability
    movie_title = serializers.ReadOnlyField(source='show.movie.title')
    screen_name = serializers.ReadOnlyField(source='show.screen_name')
    show_time = serializers.ReadOnlyField(source='show.date_time')

    class Meta:
        model = Booking
        fields = ['id', 'user', 'show', 'movie_title', 'screen_name', 'show_time', 'seat_number', 'status', 'created_at']
        read_only_fields = ['user', 'status', 'created_at']
