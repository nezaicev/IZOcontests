from django.contrib import admin
from map.models import Placemark
# Register your models here.


# class AdminPlacemark(admin.ModelAdmin):

admin.site.register(Placemark)