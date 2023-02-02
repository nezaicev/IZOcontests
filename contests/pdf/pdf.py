import os
import re

from barcode.writer import ImageWriter
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, SimpleDocTemplate, Spacer, TableStyle
from reportlab.lib import colors
import barcode
from django.conf import settings


def generate_barcode(reg_number):
    if not os.path.exists(settings.BARCODE_MEDIA_ROOT):
        os.makedirs(settings.BARCODE_MEDIA_ROOT)
    EAN = barcode.get_barcode_class('code128')
    data = list(filter(None, re.split('\D', reg_number[6:])))
    data = str(data[0])
    ean = EAN(data, writer=ImageWriter())
    try:
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
    except:
        print('Barcode is not saved')


class Pdf(object):

    def __init__(self):

        self.width, self.height = A4
        self.styles = getSampleStyleSheet()

    def coord(self, x, y, unit=1):
        """
        http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height - y * unit
        return x, y

    def run(self, fields, contest_name, alias, reg_number):

        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'pdf', alias)):
            os.mkdir(os.path.join(settings.MEDIA_ROOT, 'pdf', alias))

        self.doc = SimpleDocTemplate(os.path.join(settings.MEDIA_ROOT, 'pdf', alias,
                                                  f'{reg_number}.pdf'))
        self.story = [Spacer(1, 1 * inch)]
        self.createData(fields)
        self.contest_name = contest_name
        self.reg_number = reg_number

        self.doc.build(self.story, onFirstPage=self.createDocument)

    def createDocument(self, canvas, doc):

        self.c = canvas
        self.c.setFont('Yandex', 20)
        self.c.drawString(20, 810, self.contest_name)
        if not os.path.exists(os.path.join(settings.BARCODE_MEDIA_ROOT,
                                           '{}.png'.format(self.reg_number))):
            generate_barcode(self.reg_number)
        self.c.drawImage(
            os.path.join(settings.BARCODE_MEDIA_ROOT, f'{self.reg_number}.png'),
            340, 715)

        # normal = self.styles["Normal"]
        #
        # header_text = "<b>This is a test header</b>"
        # p = Paragraph(header_text, normal)
        # p.wrapOn(self.c, self.width, self.height)
        # p.drawOn(self.c, *self.coord(100, 12, mm))

    def createData(self, fields):

        styles = getSampleStyleSheet()
        styles.add(
            ParagraphStyle(name='Yandex', alignment=TA_JUSTIFY,
                           fontName='Yandex',
                           fontSize=12))
        styles.add(ParagraphStyle(name='YandexBold', alignment=TA_JUSTIFY,
                                  fontName='YandexBold', fontSize=12))
        pdfmetrics.registerFont(
            TTFont('Yandex',
                   os.path.join(settings.STATICFILES_DIRS[0], 'fonts',
                                'YandexSansDisplay-Regular.ttf'))
        )
        normal_style = styles['Yandex']
        bold_style = styles['Yandex']
        data = [[Paragraph(fields[i][0], normal_style),
                 Paragraph(fields[i][1], normal_style)] for i in
                range(0, len(fields))]
        table = Table(data, colWidths=[4 * cm, 14 * cm])

        table.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]))

        self.story.append(table)
