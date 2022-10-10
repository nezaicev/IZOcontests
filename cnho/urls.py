"""cnho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView, RedirectView
from django.conf.urls.static import static
from django.conf import settings
from contests.views import PageContestView, EventPageView
from contests.models import Message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('certs/', include('cert.urls')),
    path('event/', include('event.urls')),
    path('map/', include('map.urls')),
    path('users/', include('users.urls')),
    path('mailing/', include('mailing.urls')),
    path('frontend/', include('frontend.urls')),
    path('contests/', include('contests.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', PageContestView.as_view(template_name='home.html'),
         name='home'),

    # path('event/5/',  RedirectView.as_view(url='/frontend/main/')),

    # path('event/<int:pk>/',
    #      EventPageView.as_view(template_name='event/page.html'), name='event'),





]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'ЦНХО'  # default: "Django Administration"
admin.site.index_title = 'Личный кабинет '  # default: "Site administration"
admin.site.site_title = 'Личный кабинет'
