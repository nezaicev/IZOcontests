from django.contrib import admin
from content.models import Page, Video, Category
from content.forms import  ContentCreateForm
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    search_fields = ('title', 'subtitle', 'slug')


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
    filter_horizontal = ('categories',)


admin.site.register(Page, PageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Category)
