from django.contrib import admin
from django.urls import path

from .views import hello  # Import the 'hello' view from your app

urlpatterns = [
    path("", hello, name='hello'),  # Use the 'hello' view directly
]
