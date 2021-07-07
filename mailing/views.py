from django.shortcuts import render
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
from mailing.forms import UnsubscribeForm
from mailing.models import Subscriber


class UnsubscribeView(View):
    template_name = 'mailing/unsubscribe.html'
    form_class = UnsubscribeForm
    success_url = reverse_lazy('unsubscribe')

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name,
                      context={'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = UnsubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.filter(email=email).delete()
                messages.add_message(self.request, messages.ERROR,
                                     'Пользователь  с адресом {} удален из базы рассылки'.format(
                                         email))

                return HttpResponseRedirect(reverse('unsubscribe'))
            else:
                messages.add_message(self.request, messages.ERROR,
                                     'Пользователя  с адресом {} нет базе рассылки'.format(
                                         email))
                return HttpResponseRedirect(reverse('unsubscribe'))
