import re
import uuid
import os
import time
from PIL import Image, ImageOps
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, get_connection
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
import barcode
import xlwt
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from django_selectel_storage.storage import SelectelStorage, Container
import requests


def formatting_fio_participant(fio):
    fio_list = fio.split(' ')
    if len(fio_list) >= 2:
        fio = '{} {}'.format(fio_list[0].title(), fio_list[1].title())
        return fio
    else:
        return fio


def formatting_fio_teacher(fio):
    fio_list = fio.split(' ')
    if len(fio_list) >= 3:
        fio = '{} {}.{}.'.format(fio_list[0].title(),
                                 fio_list[1][0].title(),
                                 fio_list[2][0].title()
                                 )
        return fio
    else:
        return fio


def upload_img(local_url_image, path_in_container):
    storage = SelectelStorage()
    name_img = '{}.jpg'.format(uuid.uuid1())
    with open(local_url_image, 'rb') as image:
        (storage._save(os.path.join(path_in_container, name_img),
                       image.read()))
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, 'tmp', name_img)):
            os.remove(os.path.join(settings.MEDIA_ROOT, 'tmp', name_img))
    if storage.exists(os.path.join(path_in_container, name_img)):
        return storage.url(os.path.join(path_in_container, name_img))
    else:
        return None


def generate_thumb(url, size='md'):
    storage = SelectelStorage()
    result = requests.get(url)
    sizes = {'sm': (200, 200),
             'md': (900, 900)}
    if result.status_code == 200:
        with open(os.path.join(settings.MEDIA_ROOT, 'tmp', 'thumb.jpg'),
                  'wb') as f:
            f.write(result.content)
        img = Image.open(
            os.path.join(settings.MEDIA_ROOT, 'tmp', 'thumb.jpg'))
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")
        img.thumbnail(sizes[size], Image.ANTIALIAS)
        new_name_image = "{}.jpg".format(uuid.uuid1())
        path_img = os.path.join(settings.MEDIA_ROOT, 'tmp', new_name_image)
        img.save(path_img, "JPEG")
        if os.path.exists(path_img):
            return path_img
        else:
            return None


def remove_field_in_list(obj_tuple, name_field):
    fields = list(obj_tuple)
    if name_field in fields:
        fields.remove(name_field)
    return fields


def add_field_in_list(obj_tuple, name_field):
    fields = list(obj_tuple)
    if name_field not in fields:
        fields.append(name_field)
    return fields


def generate_xls(queryset, path):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(queryset[0]._meta.fields)):
        ws.write(row_num, col_num,
                 _(queryset[0]._meta.fields[col_num].verbose_name), font_style)
    font_style = xlwt.XFStyle()
    for ridx, obj in enumerate(queryset):
        ridx += 1
        for cidx, field in enumerate(obj._meta.fields):
            if field.choices:
                val = obj._get_FIELD_display(field)
                ws.write(ridx, cidx, val, font_style)
            else:
                val = str(getattr(obj, field.name))
                ws.write(ridx, cidx, val, font_style)

    wb.save(path)


def generate_barcode(reg_number):
    if not os.path.exists(settings.BARCODE_MEDIA_ROOT):
        os.makedirs(settings.BARCODE_MEDIA_ROOT)
    EAN = barcode.get_barcode_class('code128')
    data = list(filter(None, re.split('\D', reg_number[6:])))
    data = str(data[0])
    ean = EAN(data, writer=ImageWriter())
    ean.save(settings.BARCODE_MEDIA_ROOT + reg_number, options={
        'module_width': 0.2,
        'module_height': 3,
        'quiet_zone': 0.9,
        'font_size': 10,
        'text_distance': 1.5,
        'background': 'white',
        'foreground': 'black',
        'write_text': True,
        'text': '',
    }, text=None)


def generate_pdf(list, contest_name, alias, reg_number):
    width, height = A4
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(name='Yandex', alignment=TA_JUSTIFY, fontName='Yandex',
                       fontSize=12))
    styles.add(ParagraphStyle(name='YandexBold', alignment=TA_JUSTIFY,
                              fontName='YandexBold', fontSize=12))
    pdfmetrics.registerFont(
        TTFont('Yandex', os.path.join(settings.STATICFILES_DIRS[0], 'fonts',
                                      'YandexSansDisplay-Regular.ttf'))
    )
    normal_style = styles['Yandex']
    bold_style = styles['Yandex']
    data = [[Paragraph(list[i][0], normal_style),
             Paragraph(list[i][1], normal_style)] for i in range(0, len(list))]
    table = Table(data, colWidths=[4 * cm, 14 * cm])

    table.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]))
    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'pdf', alias)):
        os.mkdir(os.path.join(settings.MEDIA_ROOT, 'pdf', alias))
    c = canvas.Canvas(
        os.path.join(settings.MEDIA_ROOT, 'pdf', alias, f'{reg_number}.pdf'),
        pagesize=A4)
    c.setFont('Yandex', 20)
    c.drawString(20, 810, contest_name)
    if not os.path.exists(os.path.join(settings.BARCODE_MEDIA_ROOT,
                                       '{}.png'.format(reg_number))):
        generate_barcode(reg_number)
    c.drawImage(os.path.join(settings.BARCODE_MEDIA_ROOT, f'{reg_number}.png'),
                340, 715)

    width2, height2 = table.wrapOn(c, width, height)
    table.drawOn(c, 1.2 * cm, A4[1] - height2 - 125, 0)
    c.save()


def send_mail_contest(secret, email, reg_number, message_template,
                      name_contest, alias):
    list_emails = []
    list_emails.append(email)
    connection = get_connection(host=settings.EMAIL_CONTEST['host'],
                                port=settings.EMAIL_CONTEST['port'],
                                username=secret['user'],
                                password=secret['password'],
                                use_tls=settings.EMAIL_CONTEST['use_tls'])
    subject, from_email = name_contest, settings.EMAIL_CONTEST['from_contest']
    message = render_to_string(message_template, {'reg_number': reg_number})
    msg = EmailMultiAlternatives(subject, message, from_email, list_emails,
                                 connection=connection)
    msg.content_subtype = "html"
    try:
        if alias != 'teacher':
            attached_file = os.path.join(settings.MEDIA_ROOT, 'pdf', alias,
                                         f'{reg_number}.pdf')
        else:
            attached_file = os.path.join(settings.MEDIA_ROOT, 'zip',
                                         f'{reg_number}.zip')

        msg.attach_file(attached_file, mimetype='text/html')
        msg.send()
    except:
        msg.send()
    connection.close()


def send_mail_from_admin(secret, list_emails, message, subject):
    connection = get_connection(host=settings.EMAIL_CONTEST['host'],
                                port=settings.EMAIL_CONTEST['port'],
                                username=secret['user'],
                                password=secret['password'],
                                use_tls=settings.EMAIL_CONTEST['use_tls'])
    from_email = settings.EMAIL_CONTEST['from_contest']
    msg = EmailMultiAlternatives(subject, message, from_email, list_emails,
                                 connection=connection)
    msg.content_subtype = "html"
    msg.send()
    connection.close()


def generate_year():
    if int(time.strftime('%m', time.localtime())) <=7:
        year_contest = '{}-{} год'.format(
            int(time.strftime("%Y", time.localtime())) - 1,
            int(time.strftime("%Y", time.localtime())) + 1 - 1)
    else:
        year_contest = '{}-{} год'.format(
            int(time.strftime("%Y", time.localtime())),
            int(time.strftime("%Y", time.localtime())) + 1)
    return year_contest


def get_dependent_data_for_obj(obj, field_name):
    if hasattr(obj, field_name):
        if getattr(obj, field_name):

            return getattr(obj, field_name)
        else:
            return None


def generate_enumeration_field_by_id(obj_id, model_participant_id, field_name_generate,):
    enumeration = list(
        model_participant_id.objects.filter(participants_id=obj_id).values_list(
            field_name_generate, flat=True))

    return enumeration

# def generate_enumeration_from_inline_model(obj, model,field, enumeration=None):
#     if enumeration == None:
#         enumeration = ''
#         participants = list(
#             model.objects.filter(participants_id=obj.pk).values_list(
#                 'fio', flat=True))
#         for participant in participants:
#             if participant != participants[-1]:
#                 fios += participant + ', '
#             else:
#                 fios += participant
#         return fios
