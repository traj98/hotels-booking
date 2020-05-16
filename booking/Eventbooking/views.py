from django.shortcuts import render,redirect
from django.http import HttpResponse
from Eventbooking.forms import EventBookingForm
from .models import *

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


def eventlist(request):
    products=EventBookingdb.objects.all()
    return render(request, 'EventBookingApp/list.html', {'products':products})


def eventedit(request, id):
    product=EventBookingdb.objects.get(id=id)
    return render(request, 'EventBookingApp/edit.html', {'product':product})

def eventupdate(request, id):
    product=EventBookingdb.objects.get(id=id)
    form=EventBookingForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect("/eventlist")
    return render(request, 'EventBookingApp/edit.html', {'product':product})

def eventdelete(request, id):
    product=EventBookingdb.objects.get(id=id)
    if request.method == 'POST': 
        product.delete() 
        return redirect("/eventlist")
    return render(request, 'EventBookingApp/delete1.html', {'object':product})


def eventdelete1(request):
    return render(request, 'delete1.html')


