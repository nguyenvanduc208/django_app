from django.urls import path
from .views import fake_data

urlpatterns = [
    path("/fake", fake_data)
]
