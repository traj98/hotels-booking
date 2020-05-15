from django import forms
from .models import EventBookingdb

class EventBookingForm(forms.ModelForm):
    class Meta:
        model=EventBookingdb
        fields="__all__"
        