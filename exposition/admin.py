from django.contrib import admin

# Register your models here.
from contests.admin import InlineFormset
from exposition.models import ImageExposition, Exposition


class ImageExpositionInline(admin.StackedInline):
    readonly_fields = ('image_tag',)
    model = ImageExposition
    extra = 0


class ImageExpositionAdmin(admin.ModelAdmin):
    model=ImageExposition
    list_display = ['image_tag', 'images']


class ExpositionAdmin(admin.ModelAdmin):
    inlines = [ImageExpositionInline]
    list_display = ['title', 'start_date', 'end_date']
    list_filter = ('archive',)
    list_editable = ['end_date']

    search_fields = ('title',)


admin.site.register(Exposition, ExpositionAdmin)
admin.site.register(ImageExposition,ImageExpositionAdmin )