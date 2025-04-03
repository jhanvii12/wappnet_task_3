from django.urls import path
from .views import GoogleAuthView

urlpatterns = [
    path('auth/google/', GoogleAuthView.as_view(), name='google-auth'),
]


# from django.urls import path
# from .views import google_login, google_callback, GoogleAuthView

# urlpatterns = [
#     path("auth/google/login/", google_login, name="google-login"),
#     path("auth/google/callback/", google_callback, name="google-callback"),
#     path("auth/google/", GoogleAuthView.as_view, name='google-auth'),
# ]

# from django.contrib import admin
# from django.urls import path, include
# from socialmedia import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# urlpatterns = [
#     # Google OAuth2 endpoint
#     path('auth/google/', views.GoogleAuthView.as_view(), name='google_login'),
#     # User profile endpoint
#     path('user/', views.UserProfileView.as_view(), name='user_profile'),
#     # Social auth URLs (optional, can remove if not needed)
#     path('auth/', include('social_django.urls', namespace='social')),
#     # JWT endpoints
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]