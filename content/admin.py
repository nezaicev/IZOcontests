from django.contrib import admin
from content.models import Page, Video, Category, Publication

from content.forms import  ContentCreateForm
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    search_fields = ('title', 'subtitle', 'slug')


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
    filter_horizontal = ('categories',)


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title','year','order')
    list_editable = ('order',)
    search_fields = ('title','year')


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Publication, PublicationAdmin)
