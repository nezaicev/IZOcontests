from django.shortcuts import render
from .forms import UraoUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from rest_framework import generics
from .models import ProfileURAO
from .serializers import ProfileURAOListSerializer, ProfileURAODetailSerializer


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UraoUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'urao/signup.html'


class ProfileURAOListView(generics.ListAPIView):
    serializer_class = ProfileURAOListSerializer

    def get_queryset(self):
        # Возвращаем только профили, у которых есть работы
        return ProfileURAO.objects.filter(images__isnull=False).distinct()


class ProfileURAODetailView(generics.RetrieveAPIView):
    queryset = ProfileURAO.objects.all()
    serializer_class = ProfileURAODetailSerializer