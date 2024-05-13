import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from cert.services import get_obj_by_reg_num_from_archive
from cnho.settings import BASE_DIR
from contests.directory import NominationMYMSK


def clean_name(name):
    result=name.replace("'",'').replace('"','').replace('»','').replace('«','')
    return result


def formatting_fio(fio):
    fio = fio.upper()
    return fio


def align(text, width):
    text_aligned = ''
    lines = textwrap.wrap(text, width=width)
    for line in lines:
        text_aligned += line + '\n'
    return text_aligned


def insert_text(font_url, size, text, width, align_value, position, color,
                draw, anchor):
    if text and position:

        font = ImageFont.truetype(font_url, size=size)

        text = align(text, width)
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


def generate_cert(reg_number, blank_cert, form_values):
    font_default = os.path.join(BASE_DIR, 'static',
                                'fonts/YandexSansDisplay-Light.ttf')
    prev_field_position=None
    fio, position, school, nomination, author_name = None, None, None, None, None
    module_dir = os.getcwd()

    # obj = get_obj_by_reg_num_from_archive(reg_num, teacher, event)

    path_file = os.path.join(module_dir, settings.MEDIA_URL[1:], 'certs',
                             '{}_cert.jpg'.format(reg_number))

    img = Image.open(os.path.join(module_dir, blank_cert.blank.url[1:]))
    draw = ImageDraw.Draw(img)


    fio = insert_text(blank_cert.fio_text.font.url,
                      blank_cert.fio_text.size,
                      form_values['fio'],
                      blank_cert.fio_text.width,
                      blank_cert.fio_text.align,
                      blank_cert.fio_text.position,
                      blank_cert.fio_text.color,
                      draw,
                      blank_cert.fio_text.anchor
                      )
    prev_field_position=blank_cert.fio_text.offset if blank_cert.fio_text else 0

    blank_cert.position_text.position[1] = fio[3] + prev_field_position
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
    prev_field_position=blank_cert.position_text.offset if blank_cert.position_text else 0

    blank_cert.school_text.position[1] = fio[3]+prev_field_position

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
    prev_field_position=blank_cert.school_text.offset+school[3] if blank_cert.school_text and school else 0
    if form_values.get('city') and blank_cert.city_text:
        blank_cert.city_text.position[1] =prev_field_position

        city = insert_text(blank_cert.city_text.font.url,
                           blank_cert.city_text.size,
                           form_values['city'],
                           blank_cert.city_text.width,
                           blank_cert.city_text.align,
                           blank_cert.city_text.position,
                           blank_cert.city_text.color,
                           draw,
                           blank_cert.city_text.anchor
                           )

    prev_field_position=blank_cert.city_text.offset+city[3] if blank_cert.city_text and city else prev_field_position=blank_cert.position_text.offset+position[3]
    if form_values.get('teacher') and blank_cert.teacher_text and form_values.get('owner')=='Участник':
        blank_cert.teacher_text.position[1] = prev_field_position
        label_teacher = insert_text(font_default,
                              blank_cert.teacher_text.size,
                              'РУКОВОДИТЕЛЬ(И)',
                              blank_cert.teacher_text.width,
                              blank_cert.teacher_text.align,
                              blank_cert.teacher_text.position,
                              blank_cert.teacher_text.color,
                              draw,
                              blank_cert.teacher_text.anchor
                              )
        blank_cert.teacher_text.position[1] = prev_field_position+((img.size[1])*(blank_cert.teacher_text.size/1100))
        teacher = insert_text(blank_cert.teacher_text.font.url,
                           blank_cert.teacher_text.size,
                           form_values['teacher'],
                           blank_cert.teacher_text.width,
                           blank_cert.teacher_text.align,
                           blank_cert.teacher_text.position,
                           blank_cert.teacher_text.color,
                           draw,
                           blank_cert.teacher_text.anchor
                           )
        prev_field_position = blank_cert.teacher_text.offset+teacher[3] if blank_cert.teacher_text and teacher else 0

    if form_values.get('nomination') and blank_cert.nomination_text:
        blank_cert.nomination_text.position[1] = prev_field_position

        label_nomination = insert_text(font_default,
                                       blank_cert.nomination_text.size,
                                       'НОМИНАЦИЯ',
                                       blank_cert.nomination_text.width,
                                       blank_cert.nomination_text.align,
                                       blank_cert.nomination_text.position,
                                       blank_cert.nomination_text.color,
                                       draw,
                                       blank_cert.nomination_text.anchor
                                       )

        blank_cert.nomination_text.position[1] = prev_field_position+((img.size[1])*(blank_cert.nomination_text.size/1200))
        nomination = insert_text(font_default,
                                 blank_cert.nomination_text.size,
                                 '«{}»'.format(clean_name(NominationMYMSK.objects.get(
                                         id=form_values[
                                             'nomination']).name)
                                     ),
                                 blank_cert.nomination_text.width,
                                 blank_cert.nomination_text.align,
                                 blank_cert.nomination_text.position,
                                 blank_cert.nomination_text.color,
                                 draw,
                                 blank_cert.nomination_text.anchor
                                 )
        prev_field_position=blank_cert.nomination_text.offset+nomination[3] if blank_cert.nomination_text and nomination else 0

    if form_values.get('author_name') and blank_cert.author_name_text:
        blank_cert.author_name_text.position[1] = prev_field_position


        label_author_name = insert_text(
            font_default,
            blank_cert.author_name_text.size,
            'РАБОТА',
            blank_cert.author_name_text.width,
            blank_cert.author_name_text.align,
            blank_cert.author_name_text.position,
            blank_cert.author_name_text.color,
            draw,
            blank_cert.author_name_text.anchor
        )

        blank_cert.author_name_text.position[1] = prev_field_position+((img.size[1])*(blank_cert.author_name_text.size/1200))

        author_name = insert_text(
            blank_cert.author_name_text.font.url,
            blank_cert.author_name_text.size,
            '«{}»'.format( clean_name(form_values['author_name']) ),
            blank_cert.author_name_text.width,
            blank_cert.author_name_text.align,
            blank_cert.author_name_text.position,
            blank_cert.author_name_text.color,
            draw,
            blank_cert.author_name_text.anchor
        )

    article = blank_cert.article + ' ' + form_values['reg_number']
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

    if form_values.get('event_name') and blank_cert.event_name_text:
        event_name=insert_text(blank_cert.event_name_text.font.url,
                    blank_cert.event_name_text.size,
                    form_values['event_name'],
                    blank_cert.event_name_text.width,
                    blank_cert.event_name_text.align,
                    blank_cert.event_name_text.position,
                    blank_cert.event_name_text.color,
                    draw,
                    blank_cert.event_name_text.anchor
                    )

        # prev_field_position = blank_cert.position_text.offset if blank_cert.position_text else 0

        blank_cert.start_date_text.position[1] = event_name[3] + blank_cert.event_name_text.offset

        insert_text(blank_cert.start_date_text.font.url,
                    blank_cert.start_date_text.size,
                    form_values['start_date'],
                    blank_cert.start_date_text.width,
                    blank_cert.start_date_text.align,
                    blank_cert.start_date_text.position,


                    blank_cert.start_date_text.color,
                    draw,
                    blank_cert.start_date_text.anchor
                    )




    img.save(path_file, "JPEG")
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
                     align='center', anchor='ms')
    out.show()


