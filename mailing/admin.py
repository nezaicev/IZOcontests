from django.contrib import admin
from django.contrib.auth import get_permission_codename
from django.template.response import TemplateResponse
from django.contrib import messages
from mailing.models import Subscriber, FileXls, Email, GroupSubscribe
from mailing.utils import parse_xls
from mailing.forms import SelectRecipientsForm, EmailCreateForm, \
    SelectLetterForm
from contests import tasks


# Register your models here.


class SendEmail():
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
    # def send_selected_letter(self, request, queryset):
    #
    #     if 'apply' in request.POST:
    #         form = SelectLetterForm(request.POST)
    #         if form.is_valid():
    #             letter = Email.objects.get(id=form.cleaned_data['letters'])
    #             recipients = list(
    #                 queryset.values_list('teacher_id__email', flat=True))
    #             if recipients:
    #                 tasks.send_mail_for_subscribers.delay(recipients,
    #                                                       letter.theme,
    #                                                       letter.content)
    #                 messages.add_message(request, messages.INFO,
    #                                      'Письмо {}_{}, отправлено - {} '.format(
    #                                          letter.date,
    #                                          letter.theme,
    #                                          len(recipients)))
    #         return None
    #
    #     form = SelectLetterForm(
    #         initial={
    #             '_selected_action': queryset.values_list('id',
    #                                                      flat=True), })
    #     return TemplateResponse(request, "admin/select_letter.html",
    #                             {'items': queryset, 'form': form})
    #
    # send_selected_letter.short_description = 'Отправить выбранное письмо'
    # send_selected_letter.allowed_permissions = ('execution_all_actions',)
    #
    # def has_execution_all_actions_permission(self, request):
    #     """Does the user have the publish permission?"""
    #     opts = self.opts
    #     codename = get_permission_codename('execution_all_actions', opts)
    #     return request.user.has_perm('%s.%s' % (opts.app_label, codename))


class EmailAdmin(admin.ModelAdmin):
    form = EmailCreateForm
    list_display = ('date', 'theme', 'user')
    search_fields = ('theme', 'user')
    actions = ('send_email',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def send_email(self, request, queryset):
        if 'apply' in request.POST:
            recipients = []
            form = SelectRecipientsForm(request.POST)

            if form.is_valid():

                if form.cleaned_data['recipients'] == 'ALL':
                    recipients = list(Subscriber.objects.all().values_list(
                        'email', flat=True))
                if form.cleaned_data['recipients'] == 'MYSELF':
                    recipients.append(request.user.email)
                else:
                    recipients = list(Subscriber.objects.filter(
                        group=form.cleaned_data[
                            'recipients']).values_list(
                        'email', flat=True))

                content = queryset[0].content
                theme = queryset[0].theme
                tasks.send_mail_for_subscribers.delay(recipients, theme,
                                                      content)
                messages.add_message(request, messages.INFO,
                                     'Писем отправлено - {} '.format(
                                         len(recipients)))
            return None
        form = SelectRecipientsForm(
            initial={
                '_selected_action': queryset.values_list('id',
                                                         flat=True), })
        return TemplateResponse(request, "admin/select_recipients.html",
                                {'items': queryset, 'form': form})

    send_email.short_description = 'Отправить письмо'


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'group', 'phone_number')
    search_fields = ('email',)
    list_filter = ('group',)


class FileXlsAdmin(admin.ModelAdmin):
    list_display = ('name', 'processed')
    actions = ('insert_xls',)

    def insert_xls(self, request, queryset):
        count_dublicates = 0
        count_inserts = 0
        if 'apply' in request.POST:
            form = SelectRecipientsForm(request.POST)

            if form.is_valid():

                for obj in queryset:
                    new_subscribers = parse_xls(obj.file.url[1:],form.cleaned_data['recipients'])
                    for new_subscriber in new_subscribers:
                        subscriber, created = Subscriber.objects.get_or_create(
                            email=new_subscriber['email'],
                            group=new_subscriber['group'],
                            defaults=new_subscriber)
                        if created:
                            count_inserts += 1
                        else:
                            count_dublicates += 1
                            continue
                if count_inserts:
                    messages.add_message(request, messages.INFO,
                                         'Записей загружено - {}, кол-во дубликатов - {}'.format(
                                             count_inserts, count_dublicates))
                else:
                    messages.add_message(request, messages.INFO,
                                         'Нет новых записей')
                return None
        form = SelectRecipientsForm(
            initial={
                '_selected_action': queryset.values_list('id',
                                                         flat=True), })
        return TemplateResponse(request, "admin/insert_subscribers.html",
                                {'items': queryset, 'form': form})



    insert_xls.short_description = 'Загрузить данные'


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(FileXls, FileXlsAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(GroupSubscribe)
