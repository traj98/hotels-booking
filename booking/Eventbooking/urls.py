from django.urls import path, include
from .import views	

urlpatterns = [
    path('EventBooking/', views.EventBooking, name='EventBooking'),
    path('EventBookingSuccess/', views.EventBookingSuccess, name='EventBookingSuccess'),
    path('eventlist/', views.eventlist, name='eventlist'),
    path('eventedit/<int:id>', views.eventedit, name='eventedit'),
    path('eventupdate/<int:id>', views.eventupdate, name='eventupdate'),
    path('eventdelete/<int:id>', views.eventdelete, name='eventdelete'),
    path('eventdelete1/', views.eventdelete1, name='eventdelete1'),

]