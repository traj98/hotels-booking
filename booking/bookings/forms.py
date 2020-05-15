from django import forms
from .models import Bookingdb


class BookingForm(forms.ModelForm):
    class Meta:
        model=Bookingdb
        fields="__all__"
        