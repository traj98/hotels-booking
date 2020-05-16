from django.urls import path, include
from .import views	

urlpatterns = [
    path('Booking/', views.Booking, name='Booking'),
    path('BookingSuccess/', views.BookingSuccess, name='BookingSuccess'),
    path('list/', views.list, name='list'),

    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete1/', views.delete1, name='delete1'),


    # path('EventBooking/', views.EventBooking, name='EventBooking'),
]