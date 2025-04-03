from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from google.auth.transport import requests
from google.oauth2 import id_token
import os

User = get_user_model()

def generate_tokens(user):
    """Generate JWT tokens"""
    refresh = RefreshToken.for_user(user)
    return {
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh),
    }

class GoogleAuthView(APIView):
    def post(self, request):
        token = request.data.get("token")
        if not token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Verify Google token
            google_info = id_token.verify_oauth2_token(token, requests.Request(), os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY"))

            if "email" not in google_info:
                return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

            email = google_info["email"]
            name = google_info.get("name", "")

            user, created = User.objects.get_or_create(email=email, defaults={"username": email, "first_name": name})

            if created:
                message = "User registered successfully"
            else:
                message = "User logged in successfully"

            tokens = generate_tokens(user)

            return Response({
                "message": message,
                "access_token": tokens["access_token"],
                "refresh_token": tokens["refresh_token"],
                "user": {"email": user.email, "name": user.first_name},
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'User not authenticated'}, status=401)
        return Response({
            'id': user.id,
            'email': user.email,
            'username': user.username
        }, status=200)