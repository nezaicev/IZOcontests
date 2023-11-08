from django import forms
from django.forms import MultiValueField, CharField, MultiWidget, TextInput
from django.core.validators import RegexValidator

from contests.models import PageContest, Events, CreativeTack
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from contests.models import ParticipantVP, ParticipantMymoskvichi

class InputFile(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    data_file = forms.FileField(widget=forms.FileInput)


class SubscribeShowEventForm(forms.Form):
    teacher = forms.CharField(max_length=20)
    page_contest = forms.CharField(max_length=20)


class ConfStorageForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.TextInput)
    container = forms.CharField(widget=forms.TextInput)


class PageContestsFrom(forms.ModelForm):
    name = forms.CharField(label='Название')
    alias = forms.CharField(label='Псевдоним')
    email = forms.EmailField(label='Email')
    logo = forms.ImageField(label='Логотип')
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')
    letter = forms.CharField(widget=CKEditorUploadingWidget(), label='Информационное письмо')

    class Meta:
        fields = (
            'hide', 'order', 'name', 'alias', 'email', 'logo', 'content', 'letter', 'start_date',)
        model = PageContest


class CreativeTackAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(),
                              label='Контент')

    class Meta:
        fields = ('contest_name', 'year_contest', 'theme')
        model = CreativeTack


def get_my_choices(model, field):
    choices_list = tuple((i, i) for i in
                         model.objects.filter(field=field, access=True).values_list('data',
                                                                                    flat=True))
    return choices_list


class FIOWidget(MultiWidget):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {'label': 'ФИО'}
        widgets = [TextInput(attrs={'placeholder': 'Фамилия', 'required': 'true'}),
                   TextInput(attrs={'placeholder': 'Имя', 'required': 'true'}),
                   TextInput(attrs={'placeholder': 'Отчество', 'required': 'required'})
                   ]
        super(FIOWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            values = value.split(' ')
            return [values[0], values[1], values[2]]
        else:
            return ['', '', '']


class FIOField(MultiValueField):
    def __init__(self, *args, **kwargs):
        list_fields = [CharField(),
                       CharField(),
                       CharField()
                       ]
        super(FIOField, self).__init__(list_fields, widget=FIOWidget(), *args, **kwargs)

    def compress(self, values):
        return values[0].replace(" ", "") + ' ' + values[1].replace(" ", "") + ' ' + values[
            2].replace(" ", "")


class FIOForm(forms.ModelForm):
    fio = FIOField(label='ФИО участника')


class FormParticipantsVP(forms.ModelForm):
    fio = FIOField(label='ФИО участника')

    class Meta:
        model = ParticipantVP
        fields = ('fio', 'snils_gir','birthday', 'level')
        widgets = {
            'snils_gir': forms.TextInput(
                attrs={
                    'data-mask': '000-000-000 00',
                    'placeholder': '000-000-000 00',

                },),
            'level': forms.TextInput(
                attrs={
                    'data-mask': 'SSSSS',
                    'placeholder': '2-Б'
                }, ),
            'birthday': forms.DateInput(
                attrs={
                    'data-mask': '00.00.0000',
                    'placeholder': '23.03.1990'
                }
            )
        }


class FormParticipantsMymoskvichi(forms.ModelForm):
    fio = FIOField(label='ФИО участника')

    class Meta:
        model = ParticipantMymoskvichi
        fields = ('fio', 'snils_gir','birthday', 'level')
        widgets = {
            'snils_gir': forms.TextInput(
                attrs={
                    'data-mask': '000-000-000 00',
                    'placeholder': '000-000-000 00',

                },),
            'level': forms.TextInput(
                attrs={
                    'data-mask': 'SSSSS',
                    'placeholder': '2-Б'
                }, ),
            'birthday': forms.DateInput(
                attrs={
                    'data-mask': '00.00.0000',
                    'placeholder': '23.03.1990'
                }
            )
        }
