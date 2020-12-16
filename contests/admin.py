import os
from typing import Tuple

from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from contests.models import Artakiada, Status, Material, Level, Nomination, \
    Age, Theme, NRusheva, Mymoskvichi, Participant, TeacherExtra, \
    MymoskvichiSelect
from contests.forms import MymoskvichiForm
from django.contrib.auth.models import Group, Permission
from django.forms import ModelForm
from django.conf import settings
from contests.forms import PageContestsFrom
from contests.models import PageContest, Message
from contests import utils
from contests import tasks


# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    name=''
    form = ModelForm
    search_fields = ('reg_number', 'email', 'fio', 'fio_teacher')
    list_display = (
        'reg_number', 'fio', 'status', 'school', 'region', 'district',
        'fio_teacher')
    list_filter = ('status', 'district', 'region')
    actions = ('export_list_info',)
    exclude = ('reg_number', 'teacher', 'barcode','status')

    def __init__(self,request, *args, **kwargs):
        super().__init__(request,*args, **kwargs)
        if not Group.objects.filter(name=self.name).exists():
            group_contest = Group.objects.create(name=self.name)
            group_contest.save()

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

    def get_list_display(self, request):
        if request.user.is_superuser or request.user.groups.filter(
                name='Manager').exists():
            self.list_editable = ('status',)
            return self.list_display
        else:
            self.list_filter = ()
            group_perm = Group.objects.get(name=self.name).permissions.all()
            perm = Permission.objects.get(codename='status_view')
            if (perm in group_perm) or request.user.is_superuser:
                self.list_display = self.__class__.list_display
                return self.list_display
            else:
                list_display = list(self.list_display)
                if 'status' in self.list_display:
                    list_display.remove('status')
                    self.list_display = list_display
                return self.list_display


def save_model(self, request, obj, form, change):
    if not obj.pk:
        obj.teacher = request.user
    super().save_model(request, obj, form, change)


def get_changeform_initial_data(self, request):
    return {'city': request.user.city,
            'school': request.user.school,
            'region': request.user.region,
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
                   )}
    js = [
        'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js',
        'https://cdn.jsdelivr.net/npm/suggestions-jquery@20.3.0/dist/js/jquery.suggestions.min.js',
        '/static/dadata/js/organizations.js',
        '/static/dadata/js/city_for_admin.js']


class ArtakiadaAdmin(BaseAdmin):
    name = 'artakiada'
    list_display = (
        'reg_number', 'image_tag','fio', 'status', 'school', 'region', 'district',
        'fio_teacher')


class NRushevaAdmin(BaseAdmin):
    name = 'nrusheva'
    list_display = (
        'reg_number', 'image_tag', 'fio', 'status', 'school', 'region',
        'district',
        'fio_teacher')


class ParticipantInline(admin.StackedInline):
    model = Participant
    extra = 0


class TeacherExtraInline(admin.StackedInline):
    model = TeacherExtra
    extra = 0


class MymoskvichiAdmin(BaseAdmin):
    form = MymoskvichiForm
    model = Mymoskvichi
    name = 'mymoskvichi'
    inlines = [ParticipantInline, TeacherExtraInline]

    def response_add(self, request, obj, post_url_continue=None):
        obj.fio = obj.generate_list_participants(Participant)
        obj.fio_teacher = obj.generate_list_participants(TeacherExtra)
        obj.save()

        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        obj.fio = obj.generate_list_participants(Participant)
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


admin.site.register(MymoskvichiSelect, MymoskvichiSelectAdmin)
admin.site.register(PageContest, PageContestAdmin)
admin.site.register(Mymoskvichi, MymoskvichiAdmin)
admin.site.register(Nomination, NominationAdmin)
admin.site.register(Artakiada, ArtakiadaAdmin)
admin.site.register(NRusheva, NRushevaAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Age, AgeAdmin)
