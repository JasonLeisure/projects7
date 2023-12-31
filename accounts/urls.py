from django.urls import path
from .views import user_login, user_logout, signup

urlpatterns = [
    path("login/", user_login, name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", user_logout, name="logout"),
]
