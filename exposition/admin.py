from django.contrib import admin

# Register your models here.
from contests.admin import InlineFormset
from exposition.models import ImageExposition, Exposition


class ImageExpositionInline(admin.StackedInline):
    formset = InlineFormset
    readonly_fields = ('image_tag',)
    model = ImageExposition
    extra = 1


class ImageExpositionAdmin(admin.ModelAdmin):
    model=ImageExposition
    list_display = ['image_tag', 'images']


class ExpositionAdmin(admin.ModelAdmin):
    inlines = [ImageExpositionInline]


admin.site.register(Exposition, ExpositionAdmin)
admin.site.register(ImageExposition,ImageExpositionAdmin )