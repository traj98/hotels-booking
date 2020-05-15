# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from . models import *

class BookingAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display =('username','email','phone','age','room_number','start_booking','end_booking')
	ordering =('-username',)
	search_fields =('username','email','phone','age','room_number','start_booking','end_booking')
	list_per_page = 25
	list_filter =('username','email','phone','age','room_number','start_booking','end_booking')


admin.site.register(Bookingdb,BookingAdmin)