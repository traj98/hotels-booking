from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BookingForm
from .models import *

def Booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/BookingSuccess')
            except:
                pass
    else:
        form=BookingForm()
    return render(request,'BookingApp/booking.html', {'form':form})

def BookingSuccess(request):
    return render(request, 'BookingApp/BookingSuccess.html')

def list(request):
    products=Bookingdb.objects.all()
    return render(request, 'BookingApp/list.html', {'products':products})


def edit(request, id):
    product=Bookingdb.objects.get(id=id)
    return render(request, 'BookingApp/edit.html', {'product':product})

def update(request, id):
    product=Bookingdb.objects.get(id=id)
    form=BookingForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect("/list")
    return render(request, 'BookingApp/edit.html', {'product':product})

def delete(request, id):
    product=Bookingdb.objects.get(id=id)
    if request.method == 'POST': 
        product.delete() 
        return redirect("/list")
    return render(request, 'BookingApp/delete1.html', {'object':product})


def delete1(request):
    return render(request, 'delete1.html')

