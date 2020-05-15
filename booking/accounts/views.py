from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from .forms import *
from .models import *

# Create your views here.
def register(request):
	if request.method == 'POST':
		data = {}
		username = request.POST.get('username')
		password = request.POST.get('password')
		first_name = request.POST.get('firstname')
		last_name = request.POST.get('lastname')
		email = request.POST.get('email')
		if(request.POST.get('firstname')):
			data['firstname']=request.POST.get('firstname')
		if (request.POST.get('lastname')):
			data['lastname'] = request.POST.get('lastname')
		if (request.POST.get('mobile')):
			data['mobile'] = request.POST.get('mobile')
		if (request.POST.get('sex')):
			data['sex'] = request.POST.get('sex')
		user = User.objects.create(email=email,username=username,password=password,first_name=first_name,last_name=last_name)
		userdata = User.objects.filter(username=username)
		##if userdata:
		##	userid = userdata.id
		##userextra_data = UserProfile.objects.create(fieldname=fieldvalue,fieldname1=fieldvalue1,user=userid)
		userdata1 = UserProfile.objects.filter(user=user).update(**data)
		userdata = UserProfile.objects.get(user=user)
		return render(request, 'registration/home.html')
	else:
		return render(request, 'registration/signup.html',{})


def validate_username(request):
	username = request.GET.get('username',None)
	data = {
		'is_taken':User.objects.filter(username__iexact=username).exists()
	}
	return JsonResponse(data)


def editprofile(request,user_id):
    user1 = UserProfile.objects.get(user=user_id)
    if request.method == 'POST':
        print(request.POST)
        form = ProfileUpdateForm(request.POST, instance=user1)
        if form.is_valid():
            form.save()
            return redirect('userprofile')
    else:
        form = ProfileUpdateForm(instance=user1)
        return render(request, 'registration/edituserprofile.html',{'form': form})

def deleteprofile(request,uid):
    user1 = User.objects.get(pk=uid)
    user1.delete()
    users = UserProfile.objects.all()
    return render(request, 'registration/userlist.html', {'users': users})

def userprofile(request):
    users = UserProfile.objects.all()
    users1 = User.objects.all()
    print(users1)
    return render(request, 'registration/userlist.html', {'users': users,'users1':users1})
