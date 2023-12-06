import os

from django.contrib import admin
from django.conf import settings
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from file_resubmit.admin import AdminResubmitMixin
import qrcode
import qrcode.image.svg
# Register your models here.
from contests.admin import InlineFormset
from exposition.models import ImageExposition, Exposition, Comment
from exposition.forms import PageModelForm


class ImageExpositionInline(admin.StackedInline):
    readonly_fields = ('image_tag',)
    model = ImageExposition
    extra = 0


class ImageExpositionAdmin(AdminResubmitMixin, admin.ModelAdmin):
    model = ImageExposition
    list_display = ['image_tag', 'images']


class ExpositionAdmin(admin.ModelAdmin):
    form = PageModelForm
    actions = ['generate_qrcode_for_comments', ]
    inlines = [ImageExpositionInline]
    list_display = ['title', 'start_date', 'end_date', 'count_exp', 'count_participants']
    list_filter = ('archive',)
    list_editable = ['end_date', 'count_exp', 'count_participants']
    search_fields = ('title',)

    def generate_qrcode_for_comments(self, request,queryset):
        id_exposition=queryset[0].id
        file_location = os.path.join(settings.MEDIA_ROOT, 'tmp',f'{id_exposition}.svg')
        url = 'http://{}/comment/{}'.format(os.getenv('HOSTNAME'), id_exposition)
        img = qrcode.make(url, image_factory=qrcode.image.svg.SvgImage)
        img.save(file_location)
        try:
            response = HttpResponse(
                open(file_location, 'rb').read())
            response[
                'Content-Disposition'] = 'attachment; filename={}.svg'.format(
                id_exposition)
            response['Content-Type'] = 'application/svg'
            return response

        except:
            self.message_user(request,
                              "{} не найден (ошибка формирования)".format(
                                  file_location))
            return HttpResponseRedirect(request.get_full_path())

    generate_qrcode_for_comments.short_description = 'QR-код для отзывов'


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['author', ]


admin.site.register(Exposition, ExpositionAdmin)
admin.site.register(ImageExposition, ImageExpositionAdmin)
admin.site.register(Comment, CommentAdmin)
