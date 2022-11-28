import os
from zipfile import ZipFile
import shutil
from django import forms
from django.contrib import messages
from django.template.response import TemplateResponse
from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django_simple_export_admin.admin import DjangoSimpleExportAdmin, \
    ForceStringRender

from contests.models import Artakiada, NRusheva, Mymoskvichi, \
    ParticipantMymoskvichi, \
    TeacherExtraMymoskvichi, Archive, ShowEvent, VP, ParticipantVP, \
    TeacherExtraVP, ExtraImageVP, ExtraImageArchive, VideoArchive, VideoVP, \
    FileArchive, CreativeTack, FileVP
from contests.directory import NominationNR, NominationART, NominationMYMSK, \
    ThemeART, \
    ThemeMYMSK, ThemeRUSH, AgeRUSH, AgeMYMSK, Material, Status, Level, AgeVP, \
    NominationVP, LevelVP, DirectionVP, AgeART
from django.contrib.auth.models import Group, Permission
from django.forms import ModelForm
from django.conf import settings
from contests.forms import PageContestsFrom, ConfStorageForm, \
    CreativeTackAdminForm, InputFile
from contests.models import PageContest, Message, ModxDbimgMuz, Events
from contests import utils
from contests import tasks
from contests.services import alert_change_obj_contest
from mailing.admin import SendEmail
from event.models import Event, ParticipantEvent


# Register your models here.


class Levels(object):
    def __call__(self, value):
        return str(value)


class RegionsListFilter(admin.SimpleListFilter):
    title = ('Россия')
    parameter_name = 'russia'

    def lookups(self, request, model_admin):
        return (
            ('regions', ('Регионы')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'regions':
            return queryset.exclude(
                region__in=[1, 2])


class ArchiveInterface:

    def transfer_data(self, request, queryset):
        count_created_obj = 0
        count_updated_obj = 0
        for obj in queryset:
            event = Event.objects.filter(
                name=utils.get_dependent_data_for_obj(obj, 'contest_name'))
            if event:
                values_for_record = {
                    'event': event[0],
                    'participant': utils.get_dependent_data_for_obj(obj,
                                                                    'teacher'),
                }
                vm_record, created = ParticipantEvent.objects.update_or_create(

                    participant=obj.teacher, defaults=values_for_record,
                )
                vm_record.save()
                if created:
                    count_created_obj += 1
                else:
                    count_updated_obj += 1

            else:
                messages.add_message(request, messages.INFO,
                                     "Не найдено мероприятие {}".format(
                                         utils.get_dependent_data_for_obj(obj,
                                                                          'contest_name')))
        if count_updated_obj or count_created_obj:
            messages.add_message(request, messages.INFO,
                                 "Добавлено {}, обнавлено {}".format(
                                     count_created_obj, count_updated_obj))

    transfer_data.short_description = 'Перенести данные о мероприятие'

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

    def archived(self, request, queryset):
        count_created_obj = 0
        count_updated_obj = 0

        for obj in queryset:

            values_for_record = {

                'contest_name': utils.get_dependent_data_for_obj(obj,
                                                                 'page_contest',
                                                                 instance=False) if utils.get_dependent_data_for_obj(
                    obj, 'page_contest', instance=False) else obj.info.name,
                'year_contest': obj.year_contest,
                'image': utils.get_dependent_data_for_obj(obj, 'image'),
                'material': utils.get_dependent_data_for_obj(obj, 'material',
                                                             instance=False),
                'level': utils.get_dependent_data_for_obj(obj, 'level',
                                                          instance=False),
                'theme': utils.get_dependent_data_for_obj(obj, 'theme',
                                                          instance=False),
                'nomination': utils.get_dependent_data_for_obj(obj,
                                                               'nomination',
                                                               instance=False),
                'age': utils.get_dependent_data_for_obj(obj, 'age',
                                                        instance=False),
                'author_name': utils.get_dependent_data_for_obj(obj,
                                                                'author_name'),
                'format': utils.get_dependent_data_for_obj(obj, 'format'),
                'description': utils.get_dependent_data_for_obj(obj,
                                                                'description'),
                'program': utils.get_dependent_data_for_obj(obj, 'program'),
                'link': utils.get_dependent_data_for_obj(obj, 'link'),
                'reg_number': utils.get_dependent_data_for_obj(obj,
                                                               'reg_number'),
                'barcode': utils.get_dependent_data_for_obj(obj, 'barcode'),
                'teacher': utils.get_dependent_data_for_obj(obj, 'teacher'),
                'fio': utils.get_dependent_data_for_obj(obj, 'fio'),
                'fio_teacher': utils.get_dependent_data_for_obj(obj,
                                                                'fio_teacher'),
                'school': utils.get_dependent_data_for_obj(obj, 'school'),
                'city': utils.get_dependent_data_for_obj(obj, 'city'),
                'status': utils.get_dependent_data_for_obj(obj, 'status'),
                'region': utils.get_dependent_data_for_obj(obj, 'region'),
                'date_reg': utils.get_dependent_data_for_obj(obj, 'date_reg'),
                'district': utils.get_dependent_data_for_obj(obj, 'district'),
                'direction': utils.get_dependent_data_for_obj(obj,
                                                              'direction',
                                                              instance=False),
                'participants': utils.get_dependent_data_for_obj(obj,
                                                                 'id'),
            }
            vm_record, created = Archive.objects.update_or_create(

                reg_number=obj.reg_number, defaults=values_for_record,
            )
            if hasattr(obj, 'images'):
                vm_record.images.set(
                    [ExtraImageArchive.objects.create(image=image.image) for
                     image
                     in obj.images.select_related()])
            if hasattr(obj, 'videos'):
                vm_record.videos.set(
                    [VideoArchive.objects.create(video=video.video,
                                                 name=video.name) for
                     video
                     in obj.videos.select_related()])

            if created:
                count_created_obj += 1
            else:

                vm_record.save()
                count_updated_obj += 1

        messages.add_message(request, messages.INFO,
                             ' "{}"  новых записей  отправленно в АРХИВ, "{}" обновлено'.format(
                                 count_created_obj, count_updated_obj))

    archived.short_description = 'Отправить в Архив'


class BaseAdmin(admin.ModelAdmin, ArchiveInterface, SendEmail):
    name = ''
    form = ModelForm
    search_fields = ('reg_number', 'fio', 'fio_teacher')
    list_display = (
        'reg_number', 'fio', 'status', 'status_change', 'school', 'region',
        'district',
        'fio_teacher')
    list_filter = ('status', 'district', 'region')
    actions = ['export_list_info', 'export_as_xls', 'create_thumbs',
               'archived', 'send_selected_letter', ]
    exclude = (
        'reg_number', 'teacher', 'barcode', 'status', 'info', 'year_contest',
        'extraImage', 'status_change')

    # def create_thumbs(self, request, queryset):
    #     config = {}
    #     if 'apply' in request.POST:
    #         form = ConfStorageForm(request.POST)
    #         if form.is_valid():
    #             config = {'USERNAME': form.cleaned_data['username'],
    #                       'PASSWORD': form.cleaned_data['password'],
    #                       'CONTAINER': form.cleaned_data['container']
    #                       }
    #         urls_levels = [{'url': obj.image.url, 'level': obj.level.name} for
    #                        obj in queryset]
    #         tasks.celery_create_thumbs.delay(urls_levels, config=config)
    #         return None
    #     form = ConfStorageForm(
    #         initial={'_selected_action': queryset.values_list('id', flat=True),
    #                  'username': os.getenv('USERNAME_SELECTEL'),
    #                  'password': os.getenv('PASSWORD_SELECTEL'),
    #                  'container': os.getenv('CONTAINER_SELECTEL')
    #                  })
    #     return TemplateResponse(request, "admin/set_thumb_config.html",
    #                             {'items': queryset, 'form': form})
    #
    # create_thumbs.short_description = 'Создать превью'

    def export_list_info(self, request, queryset):
        meta = self.model._meta
        reg_number = queryset[0].reg_number
        file_location = None
        try:
            file_location = os.path.join(settings.MEDIA_ROOT, 'pdf', self.name,
                                         f'{reg_number}.pdf')
            utils.generate_barcode(queryset[0].reg_number)
            utils.generate_pdf(queryset[0].get_fields_for_pdf(),
                               queryset[0].info.name,
                               queryset[0].info.alias,
                               queryset[0].reg_number)
            response = FileResponse(open(file_location, 'rb'))
            return response

        except:
            self.message_user(request,
                              "{} не найден (ошибка формирования)".format(
                                  file_location))
            return HttpResponseRedirect(request.get_full_path())

    export_list_info.short_description = 'Скачать регистрационный лист участника'

    def get_actions(self, request):
        actions = super().get_actions(request)

        if not request.user.is_superuser:
            if 'send_selected_letter' in actions:
                del actions['send_selected_letter']

        if not request.user.is_superuser:
            if 'create_thumbs' in actions:
                del actions['create_thumbs']

        if not request.user.groups.filter(
                name='Manager').exists():
            if 'export_as_xls' in actions:
                del actions['export_as_xls']

        if not request.user.groups.filter(
                name='Manager').exists():
            if 'send_vm' in actions:
                del actions['send_vm']
        if not request.user.groups.filter(
                name='Manager').exists():
            if 'archived' in actions:
                del actions['archived']
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
            self.list_editable = ('status', 'status_change')
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
                self.list_display = utils.remove_field_in_list(
                    self.list_display, 'status_change')

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
                'fio_teacher': request.user.fio,
                'email': request.user.email,
                # 'phone_gir':request.user.phone if self.model._meta.get_field('phone_gir') else '',
                }

    def response_add(self, request, obj, post_url_continue=None):

        message = PageContest
        utils.generate_pdf(obj.get_fields_for_pdf(), obj.info.name,
                           obj.info.alias, obj.reg_number)
        tasks.simple_send_mail.delay(obj.pk, obj.__class__.__name__,
                                     "Заявка на конкурс")
        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        obj.status_change = alert_change_obj_contest(request.user, obj.teacher,
                                                     obj.status_change)
        obj.save()
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
    list_filter = (
        'level', 'status', 'district', RegionsListFilter, 'nomination',
        'region',
    )
    list_display = (
        'reg_number', 'image_tag', 'fio', 'level', 'status', 'status_change',
        'school',
        'region',
        'district',
        'fio_teacher')
    fieldsets = (
        ('Участник', {
            'fields': ('fio', 'age', 'level')
        }),
        ('Педагог', {
            'fields': ('fio_teacher',)
        }),
        ('Организация', {
            'fields': ('region', 'city', 'school', 'district',)
        }),
        ('Работа', {
            'fields': (
                'author_name', 'image', 'material', 'theme', 'nomination')
        }),
        ('Данные для ГИР (https://талантыроссии.рф/)', {

            'fields': ('email', 'birthday', 'snils_gir', 'phone_gir',
                       'address_school_gir')
        }),
    )

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.groups.filter(
                name='Manager').exists() or request.user.groups.filter(
            name='Jury').exists():
            return super(BaseAdmin, self).get_queryset(request)
        else:
            qs = super(BaseAdmin, self).get_queryset(request)
            return qs.filter(teacher=request.user)

    # def get_list_display(self, request):
    #     if request.user.groups.filter(
    #             name='Jury').exists():
    #         self.list_display = utils.remove_field_in_list(self.list_display,
    #                                                        'status')
    #         self.list_filter = utils.remove_field_in_list(self.list_filter,
    #                                                       'status')
    #         self.list_filter = self.__class__.list_filter
    #         self.list_display = utils.remove_field_in_list(self.list_display,
    #                                                        'status')
    #         self.list_filter = utils.remove_field_in_list(self.list_filter,
    #                                                       'status')
    #         return self.list_display
    #     else:
    #         return super().get_list_display(request)


class NRushevaAdmin(BaseAdmin):
    name = 'nrusheva'
    list_filter = ('level', 'status', 'district', 'region')
    list_display = (
        'reg_number', 'image_tag', 'fio', 'status', 'status_change', 'school',
        'region',
        'district',
        'fio_teacher')

    fieldsets = (
        ('Участник', {
            'fields': ('fio', 'age', 'level')
        }),
        ('Педагог', {
            'fields': ('fio_teacher',)
        }),
        ('Организация', {
            'fields': ('region', 'city', 'school', 'district',)
        }),
        ('Работа', {
            'fields': (
                'author_name', 'image', 'material', 'theme', 'nomination',
                'format', 'description')
        }),
        ('Данные для ГИР (https://талантыроссии.рф/)', {
            'fields': (
                'email', 'birthday', 'snils_gir', 'phone_gir',
                'address_school_gir')
        }),
    )


class InlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data:
                    count += 1
                    if form.cleaned_data['DELETE']:
                        count -= 1

            except AttributeError:
                pass

        if count < 1:
            raise forms.ValidationError(
                'Должен быть хотябы один участник и один педагог')


class ParticipantMymoskvichiInline(admin.StackedInline):
    formset = InlineFormset
    model = ParticipantMymoskvichi
    extra = 1


class TeacherExtraMymoskvichiInline(admin.StackedInline):
    formset = InlineFormset
    model = TeacherExtraMymoskvichi
    extra = 1


class MymoskvichiAdmin(BaseAdmin):
    model = Mymoskvichi
    name = 'mymoskvichi'
    fieldsets = (

        ('Организация', {
            'fields': ('region', 'city', 'school', 'district',)
        }),
        ('Работа', {
            'fields': (
                'author_name', 'nomination',
                'program', 'link', 'age', 'description_file', 'duration',
                'ovz')
        }),

        ('Данные для ГИР (https://талантыроссии.рф/)', {
            'fields': ('email',
                       'phone_gir', 'address_school_gir')
        }),
    )
    inlines = [ParticipantMymoskvichiInline, TeacherExtraMymoskvichiInline]
    exclude = (
        'reg_number', 'teacher', 'barcode', 'status', 'fio', 'fio_teacher',
        'participants', 'teachers', 'info', 'year_contest', 'extraImage')

    def response_add(self, request, obj, post_url_continue=None):
        if obj.generate_list_participants(ParticipantMymoskvichi):
            obj.fio = obj.generate_list_participants(ParticipantMymoskvichi)
        if obj.generate_list_participants(TeacherExtraMymoskvichi):
            obj.fio_teacher = obj.generate_list_participants(
                TeacherExtraMymoskvichi)
        obj.save()

        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        if obj.generate_list_participants(ParticipantMymoskvichi):
            obj.fio = obj.generate_list_participants(ParticipantMymoskvichi)
        if obj.generate_list_participants(TeacherExtraMymoskvichi):
            obj.fio_teacher = obj.generate_list_participants(
                TeacherExtraMymoskvichi)
        obj.save()

        return super().response_change(request, obj)


class ParticipantVPInline(admin.StackedInline):
    formset = InlineFormset
    model = ParticipantVP
    extra = 1


class TeacherExtraVPInline(admin.StackedInline):
    formset = InlineFormset
    model = TeacherExtraVP
    extra = 1


class ImageExtraVPInline(admin.StackedInline):
    model = ExtraImageVP
    extra = 0
    max_num = 15


class VideoVPInline(admin.StackedInline):
    model = VideoVP
    extra = 0


class FileVPInline(admin.StackedInline):
    model = FileVP
    extra = 0


class VPAdmin(BaseAdmin):
    model = VP
    name = 'vp'
    filter_horizontal = ('level',)
    inlines = [ParticipantVPInline, TeacherExtraVPInline, ImageExtraVPInline,
               VideoVPInline, FileVPInline]
    actions = ['download_archive_files']
    fieldsets = (

        ('Организация', {
            'fields': ('region', 'city', 'school', 'district',)
        }),
        ('Работа', {
            'fields': (
                'author_name', 'direction', 'nomination', 'level', 'ovz')
        }),
        ('Контактные данные', {
            'fields': ('email', 'phone_gir')
        }

         )

    )

    exclude = (
        'reg_number', 'teacher', 'barcode', 'status', 'fio', 'fio_teacher',
        'participants', 'teachers', 'info', 'year_contest', 'extraImage',
        'video')

    django_simple_export_admin_exports = {
        "filtered-books": {
            "label": "Выгрузить список",
            "icon": "fas fa-book",
            "fields": [
                {"field": "reg_number", "label": "Номер",
                 },
                {"field": "teacher__fio", "label": "ФИО"},
                {"field": "school", "label": "Организация"},
                {"field": "teacher__city", "label": "Город"},
                {"field": "region__name", "label": "Регион"},
                # {"field": "level", "label": "Is Published", "render":ForceStringRender()},

            ],
            "export-filtered": True,
            "permissions": [
                "contests.export_participants"],
        }
    }

    def download_archive_files(self, request, queryset):
        obj = queryset[0]
        tmp_dir = os.path.join(settings.MEDIA_ROOT, 'tmp', obj.reg_number)
        images_urls = [obj.image.url for obj in obj.images.select_related()]
        files_urls = [obj.file.url for obj in obj.files.select_related()]
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir, ignore_errors=True)

        if len(queryset) == 1:
            os.makedirs(tmp_dir)
            if images_urls:
                os.makedirs(os.path.join(tmp_dir, 'images'))
                for url in images_urls:
                    path_save = os.path.join(tmp_dir, 'images',
                                             url.split('/')[-1])
                    utils.download_file_by_url(url, path_save)
            if files_urls:
                os.makedirs(os.path.join(tmp_dir, 'files'))
                for url in files_urls:
                    path_save = os.path.join(tmp_dir, 'files',
                                             url.split('/')[-1])
                    utils.download_file_by_url(url, path_save)

            if os.listdir(os.path.join(tmp_dir, 'images')) or os.listdir(
                    os.path.join(tmp_dir, 'files')):
                shutil.make_archive(tmp_dir, 'zip', tmp_dir)
                if os.path.exists('{}.zip'.format(tmp_dir)):
                    shutil.rmtree(tmp_dir, ignore_errors=True)
                    response = HttpResponse(
                        open('{}.zip'.format(tmp_dir), 'rb').read())
                    response[
                        'Content-Disposition'] = 'attachment; filename={}.zip'.format(
                        obj.reg_number)
                    response['Content-Type'] = 'application/zip'
                    return response

        else:
            self.message_user(request,
                              "Должен быть выбран только 1 проект!",
                              messages.ERROR)
            return HttpResponseRedirect(request.get_full_path())

    download_archive_files.short_description = 'Скачать проект'

    def response_add(self, request, obj, post_url_continue=None):

        if obj.generate_list_participants(ParticipantVP):
            obj.fio = obj.generate_list_participants(ParticipantVP)
        if obj.generate_list_participants(TeacherExtraVP):
            obj.fio_teacher = obj.generate_list_participants(TeacherExtraVP)
        obj.save()

        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        if obj.generate_list_participants(ParticipantVP):
            obj.fio = obj.generate_list_participants(ParticipantVP)
        if obj.generate_list_participants(TeacherExtraVP):
            obj.fio_teacher = obj.generate_list_participants(TeacherExtraVP)
        obj.save()

        return super().response_change(request, obj)


class StatusAdmin(admin.ModelAdmin):
    model = Status
    list_display = ['name']


class MaterialAdmin(admin.ModelAdmin):
    model = Material
    list_display = ['name']


class LevelAdmin(admin.ModelAdmin):
    model = Level
    list_display = ['name']


class NominationARTAdmin(admin.ModelAdmin):
    model = NominationART
    list_display = ['name']


class NominationMYMSKAdmin(admin.ModelAdmin):
    model = NominationART
    list_display = ['name']


class AgeRUSHAdmin(admin.ModelAdmin):
    model = AgeRUSH
    list_display = ['name']


class AgeMYMSKAdmin(admin.ModelAdmin):
    model = AgeMYMSK
    list_display = ['name']


class ThemeRUSHAdmin(admin.ModelAdmin):
    model = ThemeRUSH
    list_display = ['name']


class ThemeMYMSKAdmin(admin.ModelAdmin):
    model = ThemeMYMSK
    list_display = ['name']


class PageContestAdmin(admin.ModelAdmin):
    form = PageContestsFrom


class CreativeTackAdmin(admin.ModelAdmin):
    form = CreativeTackAdminForm


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['name']


class PermissionAdmin(admin.ModelAdmin):
    model = Permission


class ImageExtraArchiveInline(admin.StackedInline):
    readonly_fields = ('image_tag',)
    model = ExtraImageArchive
    extra = 0

    def image_tag(self, obj):
        return obj.image_tag

    image_tag.short_description = 'Загружено'
    image_tag.allow_tags = True


class VideoArchiveInline(admin.StackedInline):
    model = VideoArchive
    extra = 0


class FileArchiveInline(admin.StackedInline):
    model = FileArchive
    extra = 0


class ArchiveAdmin(admin.ModelAdmin, ArchiveInterface, SendEmail):
    list_per_page = 50
    inlines = [ImageExtraArchiveInline, VideoArchiveInline, FileArchiveInline]
    model = Archive
    actions = ['export_as_xls', 'send_selected_letter',
               'load_json_data_from_file', 'transfer_data']
    list_editable = []
    list_display = ['reg_number', 'publish', 'contest_name', 'author_name',
                    'fio_teacher',
                    'teacher',
                    'rating', 'status', 'year_contest', 'certificate']
    list_filter = ('contest_name', 'publish', 'year_contest', 'status')

    search_fields = ('reg_number', 'fio', 'fio_teacher')

    exclude = ('info', 'reg_number', 'barcode', 'content', 'participants')

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.groups.filter(
                name='Manager').exists():
            return super(admin.ModelAdmin, self).get_queryset(request)
        else:
            qs = super(admin.ModelAdmin, self).get_queryset(request)
            return qs.filter(teacher=request.user)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            if 'load_json_data_from_file' in actions:
                del actions['load_json_data_from_file']
            if 'transfer_data' in actions:
                del actions['transfer_data']
        return actions

    def get_list_display(self, request):
        if request.user.is_superuser or request.user.groups.filter(
                name='Manager').exists():
            self.list_editable = ('publish', 'rating')
            self.list_filter = self.__class__.list_filter
            return self.__class__.list_display
        else:
            self.list_filter = ()
            self.list_editable = ()

            if request.user.is_superuser:
                return self.__class__.list_display
            else:
                self.list_display = utils.remove_field_in_list(
                    self.list_display, 'publish')
                self.list_display = utils.remove_field_in_list(
                    self.list_display, 'rating')
                # self.list_display=utils.add_field_in_list(self.list_display, 'certificate')
                return self.list_display

    def load_json_data_from_file(self, request, queryset):

        if 'apply' in request.POST:
            form = InputFile(request.POST, request.FILES)
            if form.is_valid():
                path_local_file = utils.handle_uploaded_file(
                    request.FILES['data_file'],
                    'json')
                messages.add_message(request, messages.INFO,
                                     'Загрузка данных из {}'.format(
                                         path_local_file))

                print(tasks.upload_data_from_file.delay(path_local_file,
                                                        os.path.join(
                                                            '{}{}'.format(
                                                                settings.PROTOCOL,
                                                                os.getenv(
                                                                    'HOSTNAME')),
                                                            'frontend/api/archive/')))

                return HttpResponseRedirect('/admin/contests/archive/')
            else:
                messages.add_message(request, messages.DEBUG,
                                     'Ошибка {}'.format(
                                         form.errors))

                return HttpResponseRedirect('/admin/contests/archive/')

        form = InputFile(initial={
            '_selected_action': queryset.values_list('id',
                                                     flat=True), })
        return TemplateResponse(request, "admin/select_file.html",
                                {'items': queryset, 'form': form})

    load_json_data_from_file.short_description = 'Загрузить данные из JSON файла'


class ShowEventAdmin(DjangoSimpleExportAdmin, admin.ModelAdmin,
                     ArchiveInterface, SendEmail):
    model = ShowEvent
    search_fields = ('reg_number', 'fio')

    list_display = (
        'reg_number', 'page_contest', 'fio', 'status', 'school', 'get_city',
        'region',
        'district',
    )
    list_filter = ('page_contest',)
    actions = ['archived', 'send_selected_letter']
    exclude = ('reg_number', 'teacher', 'barcode', 'status', 'info')

    django_simple_export_admin_exports = {
        "filtered-books": {
            "label": "Выгрузить список",
            "icon": "fas fa-book",
            "fields": [
                {"field": "reg_number", "label": "Номер",
                 },
                {"field": "page_contest__name", "label": "Мероприятие"},
                {"field": "teacher__fio", "label": "ФИО"},
                {"field": "school", "label": "Организация"},
                {"field": "teacher__city", "label": "Город"},
                {"field": "region__name", "label": "Регион"},

            ],
            "export-filtered": True,
            "permissions": [
                "contests.export_participants"],
        }
    }

    def get_city(self, obj):
        return obj.teacher.city

    get_city.short_description = 'Город'


admin.site.register(ShowEvent, ShowEventAdmin)
admin.site.register(PageContest, PageContestAdmin)
admin.site.register(Mymoskvichi, MymoskvichiAdmin)
admin.site.register(VP, VPAdmin)
admin.site.register(NominationART, NominationARTAdmin)
admin.site.register(NominationMYMSK, NominationMYMSKAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(Artakiada, ArtakiadaAdmin)
admin.site.register(NRusheva, NRushevaAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(AgeRUSH, AgeRUSHAdmin)
admin.site.register(AgeMYMSK, AgeMYMSKAdmin)
admin.site.register(ThemeRUSH, ThemeRUSHAdmin)
admin.site.register(ThemeMYMSK, ThemeMYMSKAdmin)
admin.site.register(ThemeART)
admin.site.register(Events)
admin.site.register(AgeVP)
admin.site.register(LevelVP)
admin.site.register(NominationVP)
admin.site.register(NominationNR)
admin.site.register(DirectionVP)
admin.site.register(AgeART)
admin.site.register(CreativeTack, CreativeTackAdmin)
