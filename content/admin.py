from django.contrib import admin
from content.models import Page
from content.forms import  ContentCreateForm
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    # form=ContentCreateForm
    search_fields = ('title', 'subtitle', 'slug')


admin.site.register(Page, PageAdmin)