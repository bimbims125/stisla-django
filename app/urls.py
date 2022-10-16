from django.urls import path
from app import views

urlpatterns = [
    path('dashboard', views.dashboard)
]
