import os.path
from uuid import uuid4

from sorl.thumbnail import delete
from django.conf import settings
from django.template.loader import render_to_string
from django.views.generic import ListView, TemplateView, DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from contests.models import PageContest, Message, ModxDbimgMuz, Artakiada, \
    NRusheva, Archive
from .serializers import ModxDbimgMuzSerializer
from contests import tasks
from contests.forms import SubscribeShowEventForm
from contests.services import get_show_evens_by_user, subscribe_show_event
from contests import utils


# Create your views here.
from .utils import PathAndRename


class EventPageView(DetailView):
    template_name = "event/page.html"
    model = PageContest

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_events'] = get_show_evens_by_user(self.request.user)
        return context

    def post(self, *args, **kwargs):
        form = SubscribeShowEventForm(self.request.POST)
        if self.request.method == 'POST':
            if form.is_valid():
                teacher = form.cleaned_data['teacher']
                page_contest = form.cleaned_data['page_contest']
                record_show_event = subscribe_show_event(teacher, page_contest)
                if record_show_event:
                    context = {
                        'reg_number': record_show_event.reg_number,

                    }
                    tasks.send_mail_for_subscribers.delay(
                        (record_show_event.teacher.email,),
                        record_show_event.page_contest.name,
                        record_show_event.page_contest.letter.format(
                            reg_number=record_show_event.reg_number))

            return HttpResponseRedirect(reverse('home'))


class PageContestView(ListView):
    model = PageContest

    def post(self, *args, **kwargs):
        form = SubscribeShowEventForm(self.request.POST)
        if self.request.method == 'POST':
            if form.is_valid():
                teacher = form.cleaned_data['teacher']
                page_contest = form.cleaned_data['page_contest']
                record_show_event = subscribe_show_event(teacher, page_contest)
                if record_show_event:
                    context = {
                        'reg_number': record_show_event.reg_number,

                    }
                    tasks.send_mail_for_subscribers.delay(
                        (record_show_event.teacher.email,),
                        record_show_event.page_contest.name,
                        record_show_event.page_contest.letter.format(
                            reg_number=record_show_event.reg_number))

            return HttpResponseRedirect(reverse('home'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        context['contests'] = PageContest.objects.filter(hide=False, type='1')
        context['events'] = PageContest.objects.filter(hide=False,
                                                       type='2').order_by(
            "start_date")
        context['announcements'] = PageContest.objects.filter(hide=False,
                                                              type='3')
        context['show_events'] = get_show_evens_by_user(self.request.user)
        return context


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ImageListCreate(generics.ListCreateAPIView):
    queryset = ModxDbimgMuz.objects.using(
        'vm').all()
    serializer_class = ModxDbimgMuzSerializer
    pagination_class = StandardResultsSetPagination


class RotateImageBase(APIView):
    model=None
    def get(self, request):
        user = request.user
        result=None

        if user.is_superuser or user.groups.filter(
                name__in=['Teacher', 'Manager']):
            url_image = request.query_params.get('image_url')
            angle = request.query_params.get('angle')
            reg_number = request.query_params.get('reg_number')
            obj = self.model.objects.get(reg_number=reg_number)
            file_name = url_image.split('/')[-1]
            container_name = url_image.split('/')[-2]
            local_path = os.path.join(settings.TMP_DIR, file_name)

            try:
                utils.download_file_by_url(url_image, local_path)
                utils.rotate_img(local_path, int(angle))

                with open(local_path, 'rb') as file:
                    obj.image.save('{}.{}'.format(uuid4().hex, local_path.split('.')[-1]), file)
                    result=obj.image.url
                delete(url_image)
                if os.path.exists(local_path):
                    os.remove(local_path)

                return Response({"result": result})

            except:
                return Response({"result": "Ошибка",
                                 "data": [url_image, angle, file_name,
                                          container_name, local_path]})


class RotateModelImageArtakiada(RotateImageBase):
    model = Artakiada


class RotateModelImageNRusheva(RotateImageBase):
    model = NRusheva

class RotateModelImageArchive(RotateImageBase):
    model = Archive
