import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from cert.services import get_obj_by_reg_num


def formatting_fio(fio):
    fio = fio.title()
    return fio


def align(text, width, align):
    align_prm = {'center': '{:^' + str(width) + '}',
                 'left': '{:<' + str(width) + '}',
                 'right': '{:>' + str(width) + '}'
                 }
    text_aligned = ''
    lines = textwrap.wrap(text, width=width)
    for line in lines:
        line = align_prm[align].format(line)
        text_aligned += line + '\n'
    return text_aligned


def insert_text(font_url,size,text,width,align_value,position,color,draw, ):
    if text and position:
        font = ImageFont.truetype(font_url,size=size)
        print(text,width,align_value)
        text = align(text,width,align_value)
        print(text)
        draw.multiline_text(position, text,color, align=align_value, font=font, )


def generate_cert(reg_num, blank_cert, teacher, form_values):
    module_dir = os.getcwd()

    obj = get_obj_by_reg_num(reg_num, blank_cert.contest.id, teacher)
    path_file = os.path.join(module_dir, settings.MEDIA_URL[1:], 'certs',
                             '{}_cert.jpg'.format(obj.reg_number))

    img = Image.open(os.path.join(module_dir, blank_cert.blank.url[1:]))
    draw = ImageDraw.Draw(img)
    insert_text(blank_cert.fio_text.font.url,
                blank_cert.fio_text.size,
                form_values['fio'],
                blank_cert.fio_text.width,
                blank_cert.fio_text.align,
                blank_cert.fio_text.position,
                blank_cert.fio_text.color,
                draw
                )


    img.save(path_file)
    if os.path.exists(path_file):
        return path_file
    else:
        return None


