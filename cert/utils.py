import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from cert.services import get_obj_by_reg_num_from_archive
from contests.models import MymoskvichiSelect


def formatting_fio(fio):
    fio = fio.upper()
    return fio


def align(text, width):
    text_aligned = ''
    lines = textwrap.wrap(text, width=width)
    for line in lines:

        text_aligned += line + '\n'
    return text_aligned


def insert_text(font_url,size,text,width,align_value,position,color,draw,anchor ):
    if text and position:
        font = ImageFont.truetype(font_url,size=size)
        text = align(text,width)
        draw.multiline_text(
                            position,
                            text,
                            color,
                            align=align_value,
                            font=font,
                            anchor=anchor
                            )
        return (draw.multiline_textbbox(
            position,
            text,
            font=font,
            align=align_value,
            anchor=anchor
        ))
    else:
        return None


def generate_cert(reg_num, blank_cert, teacher, form_values):
    module_dir = os.getcwd()
    obj = get_obj_by_reg_num_from_archive(reg_num, teacher)
    path_file = os.path.join(module_dir, settings.MEDIA_URL[1:], 'certs',
                             '{}_cert.jpg'.format(obj.reg_number))

    img = Image.open(os.path.join(module_dir, blank_cert.blank.url[1:]))
    draw = ImageDraw.Draw(img)
    fio=insert_text(blank_cert.fio_text.font.url,
                blank_cert.fio_text.size,
                form_values['fio'],
                blank_cert.fio_text.width,
                blank_cert.fio_text.align,
                blank_cert.fio_text.position,
                blank_cert.fio_text.color,
                draw,
                blank_cert.fio_text.anchor
                )
    print(fio)
    if fio:
        blank_cert.position_text.position[1]=fio[3]+blank_cert.fio_text.offset
        position = insert_text(blank_cert.position_text.font.url,
                          blank_cert.position_text.size,
                          form_values['position'],
                          blank_cert.position_text.width,
                          blank_cert.position_text.align,
                          blank_cert.position_text.position,
                          blank_cert.position_text.color,
                          draw,
                          blank_cert.position_text.anchor
                          )
        print(position)
        if position :
            blank_cert.school_text.position[1] = fio[3] + blank_cert.position_text.offset
            school = insert_text(blank_cert.school_text.font.url,
                                     blank_cert.school_text.size,
                                     form_values['school'],
                                     blank_cert.school_text.width,
                                     blank_cert.school_text.align,
                                     blank_cert.school_text.position,
                                     blank_cert.school_text.color,
                                     draw,
                                     blank_cert.school_text.anchor
                                     )
            if school:
                if form_values.get('nomination'):
                    blank_cert.nomination_text.position[1]=fio[3]+blank_cert.school_text.offset
                    nomination = insert_text(blank_cert.nomination_text.font.url,
                                      blank_cert.nomination_text.size,
                                      '«{}»'.format(MymoskvichiSelect.objects.get(id=form_values['nomination']).data),
                                      blank_cert.nomination_text.width,
                                      blank_cert.nomination_text.align,
                                      blank_cert.nomination_text.position,
                                      blank_cert.nomination_text.color,
                                      draw,
                                      blank_cert.nomination_text.anchor
                                      )


    article=blank_cert.article+' '+form_values['reg_number']
    insert_text(blank_cert.reg_num_text.font.url,
                blank_cert.reg_num_text.size,
                article,
                blank_cert.reg_num_text.width,
                blank_cert.reg_num_text.align,
                blank_cert.reg_num_text.position,
                blank_cert.reg_num_text.color,
                draw,
                blank_cert.reg_num_text.anchor
                )
    img.save(path_file,"JPEG")
    if os.path.exists(path_file):
        return path_file
    else:
        return None


def test_text(text):
    from PIL import Image, ImageDraw, ImageFont
    fnt = ImageFont.truetype(
        "/home/nezaicev/PycharmProjects/IZOcontests/static/fonts/YandexSansDisplay-Bold.ttf",
        40)
    out = Image.new("RGB", (600, 600), (255, 255, 255))
    d = ImageDraw.Draw(out)
    d.multiline_text((100, 100), text, font=fnt, fill=(0, 0, 0),
                     align='center',anchor='ms')
    out.show()


