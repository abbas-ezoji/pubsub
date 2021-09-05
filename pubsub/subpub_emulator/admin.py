from django.contrib import admin
from .models import *


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_id', 'latitude', 'longitude',)
    list_filter = ('name',)



