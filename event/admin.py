from django.contrib import admin, messages
from django.contrib.auth import get_permission_codename
from django.template.response import TemplateResponse
from django_changelist_toolbar_admin.admin import DjangoChangelistToolbarAdmin
from django_simple_export_admin.admin import DjangoSimpleExportAdmin

from contests import tasks
from event.models import ParticipantEvent, Event
from mailing.forms import SelectLetterForm
from mailing.models import Email
from contests import utils


class ArchivedEventFilter(admin.SimpleListFilter):
    title = 'Мероприятие'  # Название фильтра
    parameter_name = 'event'  # Параметр для URL

    def lookups(self, request, model_admin):
        # Возвращаем только мероприятия, которые не архивные
        events = Event.objects.filter(hide=False)
        return [(event.id, event.name) for event in events]

    def queryset(self, request, queryset):
        # Если фильтр применён, возвращаем отфильтрованные объекты
        if self.value():
            return queryset.filter(event__id=self.value())
        return queryset




class EventAdmin(admin.ModelAdmin):
    model = Event
    readonly_fields = ['event_url']
    list_display = ['name', 'start_date','hide', ]
    list_editable= ['hide',]

class ParticipantEventAdmin(DjangoSimpleExportAdmin, admin.ModelAdmin):
    model = ParticipantEvent
    list_display = ['reg_number', 'get_fio_participant',
                    'certificate','presence','event']
    list_filter=[ArchivedEventFilter]
    exclude = ['reg_number',]
    actions = ['send_selected_letter',]
    list_editable = ['presence']
    search_fields = ('reg_number', 'participant__fio', 'participant__email')

    django_simple_export_admin_exports = {
        "filtered-participant": {
            "label": "Выгрузить список",
            "icon": "fas fa-book",
            "fields": [
                {"field": "reg_number", "label": "Регистрационный номер",
                 },
                {"field": "event__name", "label": "Мероприятие"},

                {"field": "participant__fio", "label": "ФИО"},
                {"field": "participant__school", "label": "Организация"},
                {"field": "participant__city", "label": "Город"},
                {"field": "participant__region__name", "label": "Регион"},
                {"field": "participant__email", "label": "Email"},
                {"field": "participant__phone", "label": "Телефон"},
            ],
            "export-filtered": True,
            "permissions": [
                "event.export_participants"],
        }
    }
    @admin.action(permissions=['send_selected_letter_to_participant_event'])
    def send_selected_letter(self, request, queryset):

        if 'apply' in request.POST:
            form = SelectLetterForm(request.POST)
            if form.is_valid():
                letter = Email.objects.get(id=form.cleaned_data['letters'])
                recipients = list(
                    queryset.values_list('participant_id__email', flat=True))
                if recipients:
                    tasks.send_mail_for_subscribers.delay(recipients,
                                                          letter.theme,
                                                          letter.content)
                    messages.add_message(request, messages.INFO,
                                         'Письмо {}_{}, отправлено - {} '.format(
                                             letter.date,
                                             letter.theme,
                                             len(recipients)))
            return None

        form = SelectLetterForm(
            initial={
                '_selected_action': queryset.values_list('id',
                                                         flat=True), })
        return TemplateResponse(request, "admin/select_letter.html",
                                {'items': queryset, 'form': form})

    send_selected_letter.short_description = 'Отправить выбранное письмо'

    def has_send_selected_letter_to_participant_event_permission(self, request):
        return request.user.has_perm('event.send_selected_letter_to_participant_event')


    def get_queryset(self, request):
        if request.user.is_superuser or request.user.groups.filter(
                name='Manager').exists():
            return super(admin.ModelAdmin, self).get_queryset(request)
        else:
            qs = super(admin.ModelAdmin, self).get_queryset(request)
            return qs.filter(participant=request.user)

    def get_fio_participant(self, obj):
        return '{} - {}'.format(obj.participant.fio, obj.participant.email)

    get_fio_participant.short_description = 'Участник'

    def get_list_display(self, request):
        if request.user.is_superuser or request.user.groups.filter(
                name='Manager').exists():
            self.list_editable = ('presence',)
            self.list_filter = self.__class__.list_filter
            return self.__class__.list_display
        else:
            self.list_display = utils.remove_field_in_list(
                self.list_display, 'presence')
            self.list_filter = ()
            self.list_editable = ()

            return self.list_display



admin.site.register(Event, EventAdmin)
admin.site.register(ParticipantEvent, ParticipantEventAdmin)
