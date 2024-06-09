from django.urls import path, include
from .views import signup, home

urlpatterns = [
 path("", home, name="home"),
 path("signup/", signup, name="signup"),
 path("", include("django.contrib.auth.urls")),
]