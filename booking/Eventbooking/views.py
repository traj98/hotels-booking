from django.shortcuts import render,redirect
from django.http import HttpResponse
from Eventbooking.forms import EventBookingForm


def EventBooking(request):
    if request.method=="POST":
        form=EventBookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/EventBookingSuccess')
            except:
                pass
    else:
        form=EventBookingForm()
    return render(request,'EventBookingApp/EventBooking.html', {'form':form})

def EventBookingSuccess(request):
    return render(request, 'EventBookingApp/EventBookingSuccess.html')
