import os
from contests import utils
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from celery import shared_task
from contests import models
from contests.models import Artakiada


@shared_task
def simple_send_mail(id,class_name,subject):
    obj=getattr(models, class_name).objects.get(id=id)
    if not os.path.exists(os.path.join(settings.BARCODE_MEDIA_ROOT,
                                       '{}.png'.format(
                                           obj.reg_number))):
        utils.generate_barcode(obj.reg_number)
        utils.generate_pdf(obj.get_fields_for_pdf(), obj.name[1],
                           obj.alias, obj.reg_number)
    else:
        utils.generate_pdf(obj.get_fields_for_pdf(), obj.name[1],
                           obj.alias, obj.reg_number)
    message_template='email/letters/contest_registration.html'
    from_email=settings.DEFAULT_FROM_EMAIL
    list_emails = [obj.teacher.email]
    message = render_to_string(message_template,
                               {'reg_number': obj.reg_number,'name':obj.name[1],'email':obj.back_email})
    msg = EmailMultiAlternatives(subject, message, from_email, list_emails)
    msg.content_subtype = "html"
    attached_file = os.path.join(settings.MEDIA_ROOT, 'pdf', obj.alias, '{}.pdf'.format(obj.reg_number))
    msg.attach_file(attached_file, mimetype='text/html')
    msg.send()
