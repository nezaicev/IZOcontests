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
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView, RedirectView
from django.conf.urls.static import static
from django.conf import settings
from contests.views import PageContestView, EventPageView
from contests.models import Message
from frontend import views as frontend
urlpatterns = [

    # path('', RedirectView.as_view(url='/frontend/main/'),
    #      name='home'),

    path('', frontend.index, name='home'),
    path('', frontend.index, name='home_frontend'),
    path('vp/', frontend.index),
    path('artakiada/', frontend.index),
    path('nrusheva/', frontend.index),
    path('mymoskvichi/', frontend.index),
    path('event/', frontend.index),
    path('broadcast/', frontend.index),
    path('broadcasts/', frontend.index),

    path('frontend/', include('frontend.urls')),

    path('admin/', admin.site.urls),
    path('admin', admin.site.urls),
    path('certs/', include('cert.urls')),
    path('map', include('map.urls')),
    path('map/', include('map.urls')),
    path('users/', include('users.urls')),
    path('mailing/', include('mailing.urls')),
    path('contests/', include('contests.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    re_path(r'^frontend/event/\d', RedirectView.as_view(url='/events')),

    re_path(r'.*', frontend.index),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'ЦНХО'  # default: "Django Administration"
admin.site.index_title = 'Личный кабинет '  # default: "Site administration"
admin.site.site_title = 'Личный кабинет'
