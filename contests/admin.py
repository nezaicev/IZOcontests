import os
from django import forms
from django.template.response import TemplateResponse
from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from contests.models import Artakiada, Status, Material, Level, Nomination, \
    Age, Theme, NRusheva, Mymoskvichi, Participant, TeacherExtra, \
    MymoskvichiSelect
from contests.forms import MymoskvichiForm
from django.contrib.auth.models import Group, Permission
from django.forms import ModelForm
from django.conf import settings
from contests.forms import PageContestsFrom, ConfStorageForm
from contests.models import PageContest, Message
from contests import utils
from contests import tasks


# Register your models here.

class RegionsListFilter(admin.SimpleListFilter):
    title = ('Россия',)
    parameter_name = 'russia'

    def lookups(self, request, model_admin):
        return (
            ('regions', ('Регионы',)),
        )

    def queryset(self, request, queryset):
        if self.value() == 'regions':
            return queryset.exclude(
                region__in=[1, 2])


class BaseAdmin(admin.ModelAdmin):
    name = ''
    form = ModelForm
    search_fields = ('reg_number', 'fio', 'fio_teacher')
    list_display = (
        'reg_number', 'fio', 'status', 'school', 'region', 'district',
        'fio_teacher')
    list_filter = ('status', 'district', 'region')
    actions = ['export_list_info', 'export_as_xls', 'create_thumbs']
    exclude = ('reg_number', 'teacher', 'barcode', 'status')

    def create_thumbs(self, request, queryset):
        config = {}
        if 'apply' in request.POST:
            form = ConfStorageForm(request.POST)
            if form.is_valid():
                config = {'USERNAME': form.cleaned_data['username'],
                          'PASSWORD': form.cleaned_data['password'],
                          'CONTAINER': form.cleaned_data['container']
                          }
            urls_levels = [{'url': obj.image.url, 'level': obj.level.name} for
                           obj in queryset]
            tasks.celery_create_thumbs.delay(urls_levels, config=config)
            return None
        form = ConfStorageForm(
            initial={'_selected_action': queryset.values_list('id', flat=True),
                     'username': os.getenv('USERNAME_SELECTEL'),
                     'password': os.getenv('PASSWORD_SELECTEL'),
                     'container': os.getenv('CONTAINER_SELECTEL')
                     })
        return TemplateResponse(request, "admin/set_thumb_config.html",
                                {'items': queryset, 'form': form})

    create_thumbs.short_description = 'Создать превью'

    def export_as_xls(self, request, queryset):
        meta = self.model._meta
        path = os.path.join(settings.MEDIA_ROOT, 'xls', 'report.xls')
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}.xls'.format(
            meta)
        utils.generate_xls(queryset, path)
        response = FileResponse(open(path, 'rb'))
        return response

    export_as_xls.short_description = 'Выгрузить список Excel'

    def export_list_info(self, request, queryset):
        meta = self.model._meta
        reg_number = queryset[0].reg_number
        file_location = None
        try:
            file_location = os.path.join(settings.MEDIA_ROOT, 'pdf', self.name,
                                         f'{reg_number}.pdf')
            if os.path.exists(file_location) and os.path.getsize(
                    file_location) > 0:
                response = FileResponse(open(file_location, 'rb'))
                return response
            else:
                utils.generate_barcode(queryset[0].reg_number)
                utils.generate_pdf(queryset[0].get_parm_for_pdf(),
                                   queryset[0].name, queryset[0].alias,
                                   queryset[0].reg_number)
                response = FileResponse(open(file_location, 'rb'))
                return response

        except:
            self.message_user(request, "{} не найден".format(file_location))
            return HttpResponseRedirect(request.get_full_path())

    export_list_info.short_description = 'Скачать регистрационный лист участника'

    def get_actions(self, request):
        actions = super().get_actions(request)

        if not request.user.is_superuser:
            if 'create_thumbs' in actions:
                del actions['create_thumbs']

        if not request.user.groups.filter(
                name='Manager').exists():
            if 'export_as_xls' in actions:
                del actions['export_as_xls']
        return actions

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.groups.filter(
                name='Manager').exists():
            return super(BaseAdmin, self).get_queryset(request)
        else:
            qs = super(BaseAdmin, self).get_queryset(request)
            return qs.filter(teacher=request.user)

    def get_list_display(self, request):

        if request.user.is_superuser or request.user.groups.filter(
                name='Manager').exists():
            self.list_editable = ('status',)
            self.list_filter = self.__class__.list_filter
            return self.__class__.list_display
        else:
            self.list_filter = ()
            self.list_editable = ()

            group_perm = Group.objects.get(name='Teacher').permissions.all()
            perm = Permission.objects.get(
                codename='status_view_{}'.format(self.name))
            if (perm in group_perm) or request.user.is_superuser:
                return self.__class__.list_display
            else:
                self.list_display = utils.remove_field_in_list(
                    self.list_display, 'status')

                return self.list_display

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.teacher = request.user
        super().save_model(request, obj, form, change)

    def get_changeform_initial_data(self, request):
        return {'city': request.user.city,
                'school': request.user.school,
                'region': (request.user.region),
                'district': request.user.district,
                'fio_teacher': request.user.fio, }

    def response_add(self, request, obj, post_url_continue=None):
        utils.generate_pdf(obj.get_fields_for_pdf(), obj.name[1],
                           obj.alias, obj.reg_number)
        tasks.simple_send_mail.delay(obj.pk, obj.__class__.__name__,
                                     "Заявка на конкурс")
        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        utils.generate_pdf(obj.get_fields_for_pdf(), obj.name[1],
                           obj.alias, obj.reg_number)
        tasks.simple_send_mail.delay(obj.pk, obj.__class__.__name__,
                                     "Заявка на конкурс")
        return super().response_change(request, obj)

    class Media:
        css = {'all': ('/static/dadata/css/suggestions.min.css',
                       "https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.css",
                       )}
        js = [
            'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js',
            'https://cdn.jsdelivr.net/npm/suggestions-jquery@20.3.0/dist/js/jquery.suggestions.min.js',
            '/static/dadata/js/organizations.js',
            '/static/dadata/js/city_for_admin.js',
            "https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js",
            "https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.js",
        ]


class ArtakiadaAdmin(BaseAdmin):
    name = 'artakiada'
    list_filter = ('level', 'status', 'district', RegionsListFilter, 'region')
    list_display = (
        'reg_number', 'image_tag', 'fio', 'level', 'status', 'school',
        'region',
        'district',
        'fio_teacher')

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.groups.filter(
                name='Manager').exists() or request.user.groups.filter(
            name='Jury').exists():
            return super(BaseAdmin, self).get_queryset(request)
        else:
            qs = super(BaseAdmin, self).get_queryset(request)
            return qs.filter(teacher=request.user)

    def get_list_display(self, request):
        if request.user.groups.filter(
                name='Jury').exists():
            self.list_display = utils.remove_field_in_list(self.list_display,
                                                           'status')
            self.list_filter = utils.remove_field_in_list(self.list_filter,
                                                          'status')
            self.list_filter = self.__class__.list_filter
            self.list_display = utils.remove_field_in_list(self.list_display,
                                                           'status')
            self.list_filter = utils.remove_field_in_list(self.list_filter,
                                                          'status')
            return self.list_display
        else:
            return super().get_list_display(request)


class NRushevaAdmin(BaseAdmin):
    name = 'nrusheva'
    list_filter = ('level', 'status', 'district', 'region')
    list_display = (
        'reg_number', 'image_tag', 'fio', 'status', 'school', 'region',
        'district',
        'fio_teacher')


class InlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data:
                    count += 1
            except AttributeError:
                pass
        if count < 1:
            raise forms.ValidationError(
                'Должен быть хотябы один участник и один педагог')


class ParticipantInline(admin.StackedInline):
    formset = InlineFormset
    model = Participant
    extra = 1


class TeacherExtraInline(admin.StackedInline):
    model = TeacherExtra
    extra = 1


class MymoskvichiAdmin(BaseAdmin):
    form = MymoskvichiForm
    model = Mymoskvichi
    name = 'mymoskvichi'
    inlines = [ParticipantInline, TeacherExtraInline]
    exclude = (
        'reg_number', 'teacher', 'barcode', 'status', 'fio', 'fio_teacher')

    def response_add(self, request, obj, post_url_continue=None):
        if obj.generate_list_participants(Participant):
            obj.fio = obj.generate_list_participants(Participant)
        if obj.generate_list_participants(TeacherExtra):
            obj.fio_teacher = obj.generate_list_participants(TeacherExtra)
        obj.save()

        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        if obj.generate_list_participants(Participant):
            obj.fio = obj.generate_list_participants(Participant)
        if obj.generate_list_participants(TeacherExtra):
            obj.fio_teacher = obj.generate_list_participants(TeacherExtra)
        obj.save()

        return super().response_change(request, obj)


class StatusAdmin(admin.ModelAdmin):
    model = Status
    list_display = ['name']


class MymoskvichiSelectAdmin(admin.ModelAdmin):
    model = MymoskvichiSelect
    list_display = ['data']


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


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['name']


class PermissionAdmin(admin.ModelAdmin):
    model = Permission


admin.site.register(MymoskvichiSelect, MymoskvichiSelectAdmin)
admin.site.register(PageContest, PageContestAdmin)
admin.site.register(Mymoskvichi, MymoskvichiAdmin)
admin.site.register(Nomination, NominationAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(Artakiada, ArtakiadaAdmin)
admin.site.register(NRusheva, NRushevaAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Age, AgeAdmin)
