"""booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from accounts import views
from django.conf.urls import url

admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/',include('bookings.urls')),
    path('events/',include('Eventbooking.urls')),
    path('accounts/',include('accounts.urls')),
    url(r'^userprofile/view/$', views.userprofile,name='userprofile'),
    url(r'^userprofile/del/(?P<uid>[0-9A-Za-z_\-]+)/$', views.deleteprofile),
    url(r'^userprofile/edit/(?P<user_id>[0-9A-Za-z_\-]+)/$', views.editprofile),
            
]  + static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
