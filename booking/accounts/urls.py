from django.contrib.auth import views
from django.urls import path		
from django.conf.urls import url
from . views import *

urlpatterns =[
			path('signup',register,name='signup'),
            path('login/',views.LoginView.as_view(),name='login'),
			path('logout/',views.LogoutView.as_view(),name='logout'),
			path('password-change/',views.PasswordChangeView.as_view(),name='password_change'),
			path('password-change/done/',views.PasswordChangeDoneView.as_view(),name='password_change_done'),
			path('password-reset/',views.PasswordResetView.as_view(),name='password_reset'),
			path('password-reset/done/',views.PasswordResetDoneView.as_view(),name='password_reset_done'),
			path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
			path('reset/done/',views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
			url(r'^ajax/validate_username/$',validate_username,name='validate_username'),
			
	
]
