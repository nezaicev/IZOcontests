
from django.template.loader import render_to_string
from django.views.generic import ListView, TemplateView, DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from contests.models import PageContest, Message
from contests import tasks
from contests.forms import SubscribeShowEventForm
from contests.services import get_show_evens_by_user, subscribe_show_event


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
                        record_show_event.page_contest.letter.format(reg_number=record_show_event.reg_number))

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
                        record_show_event.page_contest.letter.format(reg_number=record_show_event.reg_number))

            return HttpResponseRedirect(reverse('home'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        context['contests'] = PageContest.objects.filter(hide=False, type='1')
        context['events'] = PageContest.objects.filter(hide=False, type='2').order_by("-start_date")
        context['announcements'] = PageContest.objects.filter(hide=False, type='3')
        context['show_events'] = get_show_evens_by_user(self.request.user)
        # context['type']=PageContest.objects.filter()
        return context
