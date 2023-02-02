import os
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, SimpleDocTemplate, Spacer
from reportlab.lib import colors


class Test(object):
    """"""
    def __init__(self):
        """Constructor"""
        self.width, self.height = letter
        self.styles = getSampleStyleSheet()

    # ----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height - y * unit
        return x, y

    # ----------------------------------------------------------------------
    def run(self):
        """
        Run the report
        """
        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'pdf', alias)):
            os.mkdir(os.path.join(settings.MEDIA_ROOT, 'pdf', alias))

        self.doc = SimpleDocTemplate(os.path.join(settings.MEDIA_ROOT, 'pdf', alias,
                         f'{reg_number}.pdf'))
        self.story = [Spacer(1, 2.5 * inch)]
        self.createLineItems()

        self.doc.build(self.story, onFirstPage=self.createDocument)

    def createDocument(self, canvas):
        self.c = canvas
        c.setFont('Yandex', 20)
        c.drawString(20, 810, contest_name)
        if not os.path.exists(os.path.join(settings.BARCODE_MEDIA_ROOT,
                                           '{}.png'.format(reg_number))):
            generate_barcode(reg_number)
        c.drawImage(
            os.path.join(settings.BARCODE_MEDIA_ROOT, f'{reg_number}.png'),
            340, 715)

        width2, height2 = table.wrapOn(c, width, height)
        table.drawOn(c, 1.2 * cm, A4[1] - height2 - 125, 0)

    def createTable(self):
        pass




        print("finished!")