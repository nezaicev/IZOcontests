from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from mailing.models import Email, Subscriber
from ckeditor.fields import RichTextField


class UploadXlsFrom(forms.Form):
    file = forms.FileField(widget=forms.FileInput)


class SelectRecipientsForm(forms.Form):
    REGION = Subscriber.REGION_CHOICES
    REGION.append(('ALL', 'Всем'))
    REGION.append(('MYSELF', 'Себе'))

    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    recipients = forms.ChoiceField(label='Получатель', widget=forms.Select, choices=REGION)


class EmailCreateForm(forms.ModelForm):
    theme = forms.CharField(label='Тема')
    content = forms.CharField(
        widget=CKEditorUploadingWidget(attrs={'name': 'ck_content'}),
        label='Контент')

    class Meta:
        fields = ('theme', 'content', 'recipient')
        model = Email


class UnsubscribeForm(forms.Form):
    email = forms.EmailField(label='Email')

    # class Meta:
    #     fields = ('email',)
    #     model = Subscriber
