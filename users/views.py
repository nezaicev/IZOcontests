from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('frontend/')


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'