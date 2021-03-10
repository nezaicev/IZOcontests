from django.contrib import admin
from map.models import Placemark
# Register your models here.


class PlacemarkAdmin(admin.ModelAdmin):
    exclude = ('image_url',)


admin.site.register(Placemark, PlacemarkAdmin)