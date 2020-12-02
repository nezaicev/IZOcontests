from django.shortcuts import render
from django.views.generic import ListView
from contests.models import PageContest
# Create your views here.


class PageContestView(ListView):
    model = PageContest