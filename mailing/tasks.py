from django.core.exceptions import ObjectDoesNotExist
from users.models import CustomUser
from celery import shared_task
from mailing.models import GroupSubscribe, Subscriber


@shared_task
def add_subscriber():
    query='select id,email,phone, region_id from users_customuser where (users_customuser.subscription = true) and (UPPER(users_customuser.email) not in(select UPPER (email) from mailing_subscriber) );'
    subscribers=CustomUser.objects.raw(query)

    try:
        moscow=GroupSubscribe.objects.get(name='Москва и МО')
        region=GroupSubscribe.objects.get(name='Регионы')
        for s in subscribers:
            if s.region.id == 1 or s.region.id == 2:
                Subscriber.objects.create(email=s.email, phone_number=s.phone,
                                          group=moscow)
            else:
                Subscriber.objects.create(email=s.email, phone_number=s.phone,
                                          group=region)
    except ObjectDoesNotExist:
        print('Необходимо создать группы Москва и МО, Регионы')




