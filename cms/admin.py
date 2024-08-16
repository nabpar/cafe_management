# from django.contrib.gis.admin import OSMGeoAdmin  # Comment this out

from django.contrib import admin
from .models import CafeCms

@admin.register(CafeCms)
class CafeCmsAdmin(admin.ModelAdmin):
    list_display = ('name','photo', 'email_1','email_2','email_3', 'mobile_no1','mobile_no2','mobile_no3','telephone','location')
