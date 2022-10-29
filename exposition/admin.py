from django.contrib import admin

# Register your models here.
from contests.admin import InlineFormset
from exposition.models import ImageExposition, Exposition


class ImageExpositionInline(admin.StackedInline):
    formset = InlineFormset
    model = ImageExposition
    extra = 1


class ExpositionAdmin(admin.ModelAdmin):
    inlines = [ImageExpositionInline]


admin.site.register(Exposition, ExpositionAdmin)
