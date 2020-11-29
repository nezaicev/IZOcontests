import os
from django.contrib import admin
from contests.models import Artakiada, Status, Material, Level, Nomination, \
    Age, Theme, NRusheva
from django.contrib.auth.models import Group, Permission
from django.forms import ModelForm
from django.conf import settings
from contests.forms import PageContestsFrom
from contests.models import PageContest
from contests import utils


# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    form = ModelForm
    list_display = ('fio', 'reg_number', 'school',
                    'region', 'district', 'teacher', 'status')
    exclude = ('reg_number', 'teacher', 'barcode')

    def get_list_display(self, request):
        if request.user.is_superuser:
            return self.list_display
        else:
            group_perm = Group.objects.get(name='Teacher').permissions.all()
            perm = Permission.objects.get(codename='status_view')
            if perm in group_perm:
                return self.list_display
            else:
                return self.list_display[:-1]

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.groups.filter(
                name='Manager').exists():
            return super(BaseAdmin, self).get_queryset(request)
        else:
            exclude = list(self.exclude)
            exclude.append('status')
            self.exclude = exclude
            qs = super(BaseAdmin, self).get_queryset(request)
            return qs.filter(teacher=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.teacher = request.user
        super().save_model(request, obj, form, change)
        if obj.pk:
            if not os.path.exists(os.path.join(settings.BARCODE_MEDIA_ROOT,
                                               '{}.png'.format(
                                                   obj.reg_number))):
                utils.generate_barcode(obj.reg_number)
                utils.generate_pdf(obj.get_fields_for_pdf(), obj.name[1],
                                   obj.alias, obj.reg_number)
            else:
                utils.generate_pdf(obj.get_fields_for_pdf(), obj.name[1],
                                   obj.alias, obj.reg_number)

    def get_changeform_initial_data(self, request):
        return {'city': request.user.city,
                'school': request.user.school,
                'region': request.user.region,
                'district': request.user.district,
                'fio_teacher': request.user.fio, }

    class Media:
        css = {'all': ('/static/dadata/css/suggestions.min.css',
                       )}
        js = [
            'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js',
            'https://cdn.jsdelivr.net/npm/suggestions-jquery@20.3.0/dist/js/jquery.suggestions.min.js',
            '/static/dadata/js/organizations.js',
            '/static/dadata/js/city_for_admin.js']


class ArtakiadaAdmin(BaseAdmin):
    name = 'artakiada'


class NRushevaAdmin(BaseAdmin):
    name = 'nrusheva'


class StatusAdmin(admin.ModelAdmin):
    model = Status
    list_display = ['name']


class MaterialAdmin(admin.ModelAdmin):
    model = Material
    list_display = ['name']


class LevelAdmin(admin.ModelAdmin):
    model = Level
    list_display = ['name']


class NominationAdmin(admin.ModelAdmin):
    model = Nomination
    list_display = ['name']


class AgeAdmin(admin.ModelAdmin):
    model = Age
    list_display = ['name']


class ThemeAdmin(admin.ModelAdmin):
    model = Theme
    list_display = ['name']


class PageContestAdmin(admin.ModelAdmin):
    form = PageContestsFrom


admin.site.register(PageContest, PageContestAdmin)
admin.site.register(Nomination, NominationAdmin)
admin.site.register(Artakiada, ArtakiadaAdmin)
admin.site.register(NRusheva, NRushevaAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Age, AgeAdmin)
admin.site.register(Theme, ThemeAdmin)
