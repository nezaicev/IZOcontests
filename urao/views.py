from django.shortcuts import render
from .forms import UraoUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UraoUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'urao/signup.html'