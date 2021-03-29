from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy, reverse
from django.http import FileResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import generic, View
from cert.forms import SearchRegNumForm, ConfirmationUserDataForm, \
    ConfirmationUserDataExtraForm
from cert.services import get_obj_by_reg_num, get_blank_cert
from cert.utils import generate_cert


# Create your views here.


class SearchRegNumView(generic.FormView):
    template_name = 'cert/cert.html'
    form_class = SearchRegNumForm
    success_url = reverse_lazy('confirmation_data_view')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render(request, template_name=self.template_name,
                          context={'form': self.form_class})
        else:
            return HttpResponseRedirect(reverse('login'))

    def form_valid(self, form):
        self.request.session['reg_number'] = form.cleaned_data['reg_number']
        self.request.session['event'] = form.cleaned_data['event']
        participant = get_obj_by_reg_num(self.request.session['reg_number'],
                                         self.request.session['event'],
                                         self.request.user)
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
        context = {}
        participant = get_obj_by_reg_num(self.request.session['reg_number'],
                                         self.request.session['event'],
                                         self.request.user)
        if participant:
            if participant.__class__.alias == 'mymoskvichi':
                self.form=ConfirmationUserDataExtraForm
                self.initial_data={'reg_number': participant.reg_number,
                     'status': participant.status.id if participant.status else participant.status,
                     }
            else:
                self.form = ConfirmationUserDataForm
                self.initial_data={'reg_number': participant.reg_number,
                     'fio': participant.fio,
                     'level': participant.level.id,
                     'status': participant.status.id if participant.status else participant.status,
                     }

        if request.method == 'GET':
            self.form=self.form(self.initial_data)
            context['form'] = self.form
            return render(request, 'cert/cert_confirmation.html', context)
        if request.method == 'POST':
            self.form=self.form(request.POST)
            if self.form.is_valid():
                event = request.session.get('event')
                status = self.form.cleaned_data['status']
                reg_number = self.form.cleaned_data['reg_number']
                try:
                    blank = get_blank_cert(event, status)
                    form_values = self.form.cleaned_data
                    path_cert = generate_cert(reg_number, blank, self.request.user,
                                              form_values)
                    if path_cert:
                        response = FileResponse(open(path_cert, 'rb'))
                        return response
                except ObjectDoesNotExist:
                    messages.add_message(self.request, messages.ERROR,
                                         'Для участника с номером {} нет доступных сертификатов'.format(
                                             request.session.get(
                                                 'reg_number')))
                    return HttpResponseRedirect(reverse('search_cert'))
            else:
                messages.add_message(self.request, messages.ERROR,
                                     'Ошибка ввода данных'.format(
                                         request.session.get('reg_number')))
                return HttpResponseRedirect(reverse('confirmation_data_view'))

        else:

            messages.add_message(self.request, messages.ERROR,
                                 'Участник с номером {} не найден'.format(
                                     request.session.get('reg_number')))
            return HttpResponseRedirect(reverse('search_cert'))
