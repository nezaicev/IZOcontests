import os
import xlrd
from django.contrib import admin
from django.contrib import messages
from mailing.models import Subscriber, FileXls
from mailing.utils import parse_xls
from mailing.forms import UploadXlsFrom


# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email','region','phone_number')


class FileXlsAdmin(admin.ModelAdmin):
    list_display = ('name','processed')
    actions = ('insert_xls',)

    def insert_xls(self, request, queryset):
        count_dublicates = 0
        count_inserts = 0

        for obj in queryset:
            new_subscribers = parse_xls(obj.file.url[1:])
            for new_subscriber in new_subscribers:
                subscriber, created = Subscriber.objects.get_or_create(
                    email=new_subscriber['email'],
                    defaults=new_subscriber)
                if created:
                    count_inserts += 1
                else:
                    count_dublicates += 1
                    continue
        if count_inserts:
            messages.add_message(request, messages.INFO,
                                 'Записей загружено - {}, кол-во дубликатов - {}'.format(
                                     count_inserts, count_dublicates))
        else:
            messages.add_message(request, messages.INFO,
                                 'Нет новых записей')

    insert_xls.short_description = 'Загрузить данные'


admin.site.register(Subscriber,SubscriberAdmin)
admin.site.register(FileXls, FileXlsAdmin)
