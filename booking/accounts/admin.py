# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from . models import *

class UserAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display =('firstname','lastname','mobile','sex')
	ordering =('-firstname',)
	search_fields =('firstname','lastname','mobile','sex')
	list_per_page = 25
	list_filter =('firstname','lastname','mobile','sex')


admin.site.register(UserProfile,UserAdmin)