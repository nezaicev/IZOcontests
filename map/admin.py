from django.contrib import admin
from map.models import Placemark
# Register your models here.


class PlacemarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url','coordinates')
    search_fields = ('title','video_url','coordinates')
    exclude = ('image_url',)


admin.site.register(Placemark, PlacemarkAdmin)