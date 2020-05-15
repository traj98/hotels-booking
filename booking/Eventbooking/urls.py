from django.urls import path, include
from .import views	

urlpatterns = [
    path('EventBooking/', views.EventBooking, name='EventBooking'),
    path('EventBookingSuccess/', views.EventBookingSuccess, name='EventBookingSuccess'),
]