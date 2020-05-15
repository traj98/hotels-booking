from django.urls import path, include
from .import views	

urlpatterns = [
    path('Booking/', views.Booking, name='Booking'),
    path('BookingSuccess/', views.BookingSuccess, name='BookingSuccess'),

    # path('EventBooking/', views.EventBooking, name='EventBooking'),
]