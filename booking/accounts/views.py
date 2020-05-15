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
