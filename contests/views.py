import os.path
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

from contests.models import PageContest, Message, ModxDbimgMuz
from .serializers import ModxDbimgMuzSerializer
from contests import tasks
from contests.forms import SubscribeShowEventForm
from contests.services import get_show_evens_by_user, subscribe_show_event
from contests import utils


# Create your views here.
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


class RotateImage(APIView):

    def get(self, request):
        user = request.user
        if user.is_superuser or user.groups.filter(
                name__in=['Teacher', 'Manager']):
            url_image = request.query_params.get('image_url')
            angle = request.query_params.get('angle')
            file_name = url_image.split('/')[-1]
            container_name = url_image.split('/')[-2]
            local_path = os.path.join(settings.TMP_DIR, file_name)
            try:
                utils.download_file_by_url(url_image, local_path)
                utils.rotate_img(local_path, int(angle))
                result = utils.replace_file_to_selectel(local_path,
                                                        container_name)


                return Response({"result": result})

            except:
                return Response({"result": "Ошибка",
                                 "data": [url_image, angle, file_name,
                                          container_name, local_path]})

        #
        # if is_archive is None:
        #     expositions = Exposition.objects.all()
        # else:
        #     expositions = Exposition.objects.filter(archive=is_archive)
        # serializer = ExpositionListSerializer(expositions, many=True)
        # return Response(serializer.data)
