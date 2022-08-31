import os
import json
import math
import logging
from contests import utils

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from celery import shared_task
from django_selectel_storage.storage import SelectelStorage, Container
from contests import models
from contests.utils import generate_thumb, authenticate_user

logger = logging.getLogger(__name__)

f_handler = logging.FileHandler('upload_data_from_file.log')
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter(
    "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)


@shared_task
def upload_data_from_file(path_file_data, api_url):
    count_uploaded_files = 0
    logger.info('file - {}, url - {}'.format(path_file_data, api_url))

    with open(path_file_data) as file:
        data = json.load(file)
    session, response = authenticate_user(os.getenv('USERNAME'),
                                          os.getenv('PASSWORD'))
    logger.info('authenticate_status - {}'.format(response.status_code))

    for item in data:
        result = session.post(api_url, item)
        if result:
            count_uploaded_files += 1

        logger.info('result - {}'.format(result.content))
        result.raise_for_status()
    logger.warning('report: input - {} result - {}'.format(len(data),
                                                        count_uploaded_files))


@shared_task
def celery_create_thumbs(urls_levels, config):
    if config['USERNAME'] == '':
        storage = SelectelStorage()
    else:
        storage = SelectelStorage()
        storage.config = config
        storage.container = Container(config)

    for obj in urls_levels:
        path_thumb = generate_thumb(obj)
        name_img = obj['level'].replace(' ', '_') + '_' + \
                   obj['url'].split('/')[-1]
        with open(path_thumb, 'rb') as image:
            (storage._save(os.path.join(name_img), image.read()))
            os.remove(os.path.join(settings.MEDIA_ROOT, 'tmp', name_img))
    else:
        print('Объект не содержит атрибута "image"')


@shared_task
def simple_send_mail(id, class_name, subject):
    obj = getattr(models, class_name).objects.get(id=id)
    # message_template = 'email/letters/contest_registration.html'
    message = obj.info.letter.format(reg_number=obj.reg_number,
                                     name=obj.info.name, email=obj.info.email)
    from_email = settings.DEFAULT_FROM_EMAIL
    list_emails = [obj.teacher.email]
    # message = render_to_string(message,
    #                            {'reg_number': obj.reg_number,
    #                             'name': obj.info.name, 'email': obj.info.email})
    msg = EmailMultiAlternatives(subject, message, from_email, list_emails)
    msg.content_subtype = "html"
    attached_file = os.path.join(settings.MEDIA_ROOT, 'pdf', obj.info.alias,
                                 '{}.pdf'.format(obj.reg_number))
    msg.attach_file(attached_file, mimetype='text/html')
    msg.send()


@shared_task
def send_mail_for_subscribers(emails, theme, content):
    from_email = settings.DEFAULT_FROM_EMAIL
    list_emails = emails
    context = {
        'link': 'http://konkurs.shkola-nemenskogo.ru/mailing/unsubscribe/'
    }
    content += render_to_string('mailing/footer_message.html', context)
    list_emails_sliced = slice_list_email(list_emails, 1)
    for slice_emails in list_emails_sliced:
        msg = EmailMultiAlternatives(theme, content, from_email, slice_emails)
        msg.content_subtype = "html"
        msg.send()


def slice_list_email(list_emails, count):
    step = 0
    emails = []
    for i in range(math.ceil(len(list_emails) / count)):
        emails.append(list_emails[step:step + count])
        step += count
    return emails
