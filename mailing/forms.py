from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from mailing.models import Email, Subscriber, GroupSubscribe
from ckeditor.fields import RichTextField


class UploadXlsFrom(forms.Form):
    file = forms.FileField(widget=forms.FileInput)


class SelectLetterForm(forms.Form):
    letters = Email.objects.all().values_list('id','date')
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    letters = forms.ChoiceField(label='Письмо', widget=forms.Select,
                                choices=letters)


class SelectRecipientsForm(forms.Form):
    groups = GroupSubscribe.objects.all().values_list('id', 'name')
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    recipients = forms.ChoiceField(label='Группа', widget=forms.Select,
                                   choices=groups)


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
