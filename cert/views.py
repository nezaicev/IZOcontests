import os
from django.utils import dateformat
from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy, reverse
from django.http import  HttpResponseRedirect
from django.contrib import messages
from cert.forms import SearchRegNumForm, \
    BaseConfirmationUserDataForm, ConfirmationUserDataExtraForm, \
    ConfirmationUserDataEventForm
from django.views import generic, View
from cert.services import get_obj_by_reg_num_from_archive, get_blank_cert
from cert.utils import generate_cert
from event.models import ParticipantEvent


# Create your views here.

class SearchRegNumView(generic.FormView):
    template_name = 'cert/cert.html'
    form_class = SearchRegNumForm
    success_url = reverse_lazy('confirmation_data_view')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # Поиск участника в Архиве
            if request.GET.get('reg_number') and request.GET.get('event'):
                self.request.session['reg_number'] = request.GET.get(
                    'reg_number')
                self.request.session['event'] = request.GET.get('event')
                participant = get_obj_by_reg_num_from_archive(
                    self.request.session['reg_number'],
                    self.request.user,
                    self.request.session['event'])
                if participant:
                    self.request.session[
                        'contest'] = participant.__class__.__name__
                    self.request.session['participant_id'] = participant.id
                    return HttpResponseRedirect(
                        reverse('confirmation_data_view'))

            return render(request, template_name=self.template_name,
                          context={'form': self.form_class})
        else:
            return HttpResponseRedirect(reverse('login'))

    def form_valid(self, form):
        self.request.session['reg_number'] = form.cleaned_data['reg_number']
        self.request.session['event'] = form.cleaned_data['event']
        participant = get_obj_by_reg_num_from_archive(
            self.request.session['reg_number'],
            self.request.user,
            self.request.session['event'])
        if participant:
            self.request.session['contest'] = participant.__class__.__name__
            self.request.session['participant_id'] = participant.id
            return super().form_valid(form)
        else:
            messages.add_message(self.request, messages.ERROR,
                                 'Участник с номером {} не найден'.format(
                                     self.request.session.get('reg_number')))
            return HttpResponseRedirect(reverse('search_cert'))


class ConfirmationUserDataView(View):

    def dispatch(self, request, *args, **kwargs):
        self.form = BaseConfirmationUserDataForm
        context = {}
        participant = get_obj_by_reg_num_from_archive(
            self.request.session['reg_number'], self.request.user,
            request.session.get('event'))
        self.initial_data = {'reg_number': participant.reg_number,
                             'status': participant.status.id if participant.status else participant.status,
                             'school': participant.school,
                             'year': participant.year_contest,

                             }
        if participant:
            if participant.contest_name != os.getenv('MYMOSKVICHI'):
                self.initial_data['fio'] = participant.fio if len(
                    participant.fio) <= 100 else 'Творческий коллектив'
                self.initial_data['position'] = participant.level
                self.initial_data['author_name'] = participant.author_name
                self.initial_data['city'] = '{}, {}'.format(participant.region,
                                                            participant.city)
                self.initial_data['teacher'] = participant.fio_teacher
            else:
                self.initial_data['fio'] = participant.fio if len(
                    participant.fio) <= 100 else 'Творческий коллектив'
                self.initial_data['author_name'] = participant.author_name
                self.initial_data['city'] = '{}, {}'.format(participant.region,
                                                            participant.city)
                self.initial_data['teacher'] = participant.fio_teacher
                self.form = ConfirmationUserDataExtraForm

        if request.method == 'GET':
            self.form = self.form(self.initial_data)
            context['form'] = self.form
            return render(request, 'cert/cert_confirmation.html', context)
        if request.method == 'POST':
            self.form = self.form(request.POST)
            print(self.form.errors)
            if self.form.is_valid():
                event = request.session.get('event')
                status = self.form.cleaned_data['status']
                year = self.form.cleaned_data['year']
                reg_number = self.form.cleaned_data['reg_number']
                try:
                    blank = get_blank_cert(event, status, year)
                    form_values = self.form.cleaned_data
                    path_cert = generate_cert(reg_number, blank,
                                              form_values)
                    if path_cert:
                        return HttpResponseRedirect(
                            os.path.join(settings.MEDIA_URL, 'certs',
                                         path_cert.split('/')[-1]))

                except ObjectDoesNotExist:
                    messages.add_message(self.request, messages.ERROR,
                                         'Для участника с номером {} нет доступных сертификатов'.format(
                                             request.session.get(
                                                 'reg_number')))
                    return HttpResponseRedirect(reverse('search_cert'))
            else:
                messages.add_message(self.request, messages.ERROR,
                                     'Одно из полей ввода прывысило максимальную длинну')
                return HttpResponseRedirect(reverse('confirmation_data_view'))

        else:

            messages.add_message(self.request, messages.ERROR,
                                 'Участник с номером {} не найден'.format(
                                     request.session.get('reg_number')))
            return HttpResponseRedirect(reverse('search_cert'))


class ConfirmationParticipantCertEvent(View):

    def dispatch(self, request, *args, **kwargs):
        self.form = ConfirmationUserDataEventForm
        context = {}
        if request.method == 'GET':
            record_event = ParticipantEvent.objects.get(
                reg_number=request.GET.get('reg_number'))
            request.session['reg_number']=request.GET.get('reg_number')


            start_date =dateformat.format(record_event.event.start_date, settings.DATE_FORMAT)

            self.form = self.form(
                {   'event_name': record_event.event.name,
                    'start_date': start_date,
                    'fio': record_event.participant.fio,
                    'reg_number': record_event.reg_number,
                    'school': record_event.participant.school,
                    'city': '{}, {}'.format(record_event.participant.region,
                                            record_event.participant.city),

                }
            )
            context['form'] = self.form
            return render(request, 'cert/cert_confirmation.html', context)

        if request.method == 'POST':
            record_event=ParticipantEvent.objects.get(reg_number=request.session.get('reg_number'))
            self.form = self.form(request.POST)
            print(self.form.errors)
            if self.form.is_valid():
                form_values = self.form.cleaned_data
                path_cert=generate_cert(record_event.reg_number, record_event.event.certificate, form_values, )
                if path_cert:
                        return HttpResponseRedirect(
                            os.path.join(settings.MEDIA_URL, 'certs',
                                         path_cert.split('/')[-1]))
            else:
                messages.add_message(self.request, messages.ERROR,
                                     'Ошибка! {}'.format(self.form.errors))


