import os
from django import forms
from django.contrib import messages
from django.template.response import TemplateResponse
from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from contests.models import Artakiada, NRusheva, Mymoskvichi, \
    ParticipantMymoskvichi, \
    TeacherExtraMymoskvichi, Archive, ShowEvent, VP, ParticipantVP, \
    TeacherExtraVP, ExtraImageVP, ExtraImageArchive, VideoArchive, VideoVP, FileArchive, CreativeTack
from contests.directory import NominationNR, NominationART, NominationMYMSK, \
    ThemeART, \
    ThemeMYMSK, ThemeRUSH, AgeRUSH, AgeMYMSK, Material, Status, Level, AgeVP, \
    NominationVP, LevelVP, DirectionVP, AgeART
from django.contrib.auth.models import Group, Permission
from django.forms import ModelForm
from django.conf import settings
from contests.forms import PageContestsFrom, ConfStorageForm, CreativeTackAdminForm
from contests.models import PageContest, Message, ModxDbimgMuz, Events
from contests import utils
from contests import tasks
from mailing.admin import SendEmail


# Register your models here.


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
                                                                 'page_contest') if utils.get_dependent_data_for_obj(
                    obj, 'page_contest') else obj.info.name,
                'year_contest': obj.year_contest,
                'image': utils.get_dependent_data_for_obj(obj, 'image'),
                'material': utils.get_dependent_data_for_obj(obj, 'material'),
                'level': utils.get_dependent_data_for_obj(obj, 'level'),
                'theme': utils.get_dependent_data_for_obj(obj, 'theme'),
                'nomination': utils.get_dependent_data_for_obj(obj,
                                                               'nomination'),
                'age': utils.get_dependent_data_for_obj(obj, 'age'),
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
                                                              'direction'),

            }
            vm_record, created = Archive.objects.get_or_create(

                reg_number=obj.reg_number, defaults=values_for_record,
            )
            if hasattr(obj, 'images'):
                vm_record.images.set(
                    [ExtraImageArchive.objects.create(image=image.image) for
                     image
                     in obj.images.select_related()])
            if hasattr(obj, 'videos'):
                vm_record.videos.set(
                    [VideoArchive.objects.create(video=video.video, name=video.name) for
                     video
                     in obj.videos.select_related()])

            if created:
                count_created_obj += 1
            else:
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
        'reg_number', 'fio', 'status', 'school', 'region', 'district',
        'fio_teacher')
    list_filter = ('status', 'district', 'region')
    actions = ['export_list_info', 'export_as_xls', 'create_thumbs', 'send_vm',
               'archived', 'send_selected_letter', ]
    exclude = (
        'reg_number', 'teacher', 'barcode', 'status', 'info', 'year_contest',
        'extraImage')

    def send_vm(self, request, queryset):

        for obj in queryset:
            path_thumb = utils.generate_thumb(obj.image.url)
            if path_thumb:
                path_file_selectel = utils.upload_img(path_thumb, 'thumbs')

                values_for_update = {
                    'competition1': obj.__class__.alias,
                    'material': obj.material.name,
                    'fiocompetitor': utils.formatting_fio_participant(obj.fio),
                    'agecompetitor': obj.level.name,
                    'pathfile': path_file_selectel,
                    'fioteacher': utils.formatting_fio_teacher(
                        obj.fio_teacher),
                    'shcoolname': obj.school,
                    'cityname': obj.teacher.region.name,
                    'picturename': obj.author_name if hasattr(obj,
                                                              'author_name') else obj.theme.name if (
                            hasattr(obj, 'theme') and hasattr(obj.theme,
                                                              'name')) else '',
                    'year': obj.year_contest.split('-')[1].split(' ')[0],
                    'temaname': obj.theme.name if (
                            hasattr(obj, 'theme') and hasattr(obj.theme,
                                                              'name')) else obj.nomination if hasattr(
                        obj, 'nomination') else ''

                }
                vm_record, created = ModxDbimgMuz.objects.using(
                    'vm').update_or_create(
                    oldname=obj.reg_number, defaults=values_for_update
                )
                if created:
                    messages.add_message(request, messages.INFO,
                                         'Запись "{}" отправленна в ВМ'.format(
                                             obj.reg_number))
                else:
                    messages.add_message(request, messages.INFO,
                                         'Запись "{}" обновлена в ВМ'.format(
                                             obj.reg_number))

                os.remove(path_thumb)

    send_vm.short_description = 'Отправить в ВМ'

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
                                   queryset[0].info.name,
                                   queryset[0].info.alias,
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

        message = PageContest
        utils.generate_pdf(obj.get_fields_for_pdf(), obj.info.name,
                           obj.info.alias, obj.reg_number)
        tasks.simple_send_mail.delay(obj.pk, obj.__class__.__name__,
                                     "Заявка на конкурс")
        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        utils.generate_pdf(obj.get_fields_for_pdf(), obj.info.name,
                           obj.info.alias, obj.reg_number)
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


class VideoVPInline(admin.StackedInline):
    model = VideoVP
    extra = 0


class VPAdmin(BaseAdmin):
    model = VP
    name = 'vp'
    inlines = [ParticipantVPInline, TeacherExtraVPInline, ImageExtraVPInline, VideoVPInline]
    exclude = (
        'reg_number', 'teacher', 'barcode', 'status', 'fio', 'fio_teacher',
        'participants', 'teachers', 'info', 'year_contest', 'extraImage', 'video')

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
    form=CreativeTackAdminForm

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
    actions = ['export_as_xls', 'send_selected_letter', ]
    list_editable = []
    list_display = ['reg_number','publish', 'contest_name', 'author_name', 'fio_teacher',
                    'teacher',
                    'rating','status', 'year_contest','certificate']
    list_filter = ('contest_name', 'publish','year_contest', 'status')

    search_fields = ('reg_number', 'fio',  'fio_teacher')



    exclude = ('info','reg_number', 'barcode', 'content')

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.groups.filter(
                name='Manager').exists():
            return super(admin.ModelAdmin, self).get_queryset(request)
        else:
            qs = super(admin.ModelAdmin, self).get_queryset(request)
            return qs.filter(teacher=request.user)

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


class ShowEventAdmin(admin.ModelAdmin, ArchiveInterface, SendEmail):
    model = ShowEvent
    search_fields = ('reg_number', 'fio')

    list_display = (
        'reg_number', 'page_contest', 'fio', 'status', 'school', 'region',
        'district',
    )
    list_filter = ('page_contest',)
    actions = ['archived', 'export_as_xls', 'send_selected_letter']
    exclude = ('reg_number', 'teacher', 'barcode', 'status', 'info')

    def get_name(self, obj):
        if obj.info:
            return obj.info.name
        else:
            return ''


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