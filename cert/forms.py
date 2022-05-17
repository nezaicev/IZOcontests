from django import forms
from contests.models import Level
from contests.directory import NominationMYMSK
from contests.models import Events
from django.forms.widgets import ChoiceWidget, Input
from django.contrib import messages


class SearchRegNumForm(forms.Form):
    event = forms.ChoiceField(label='Конкурс|Мероприятие',

                              )
    reg_number = forms.CharField(label='Регистрационный номер', max_length=20)

    # class Meta:
    #     fields = ('reg_number','event')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the query here
        MYQUERY = Events.objects.all().values_list('id', 'name')
        self.fields['event'] = forms.ChoiceField(choices=(*MYQUERY,),
                                                 label='Конкурс|Мероприятие')


class BaseConfirmationUserDataForm(forms.Form):
    field_order = ('reg_number', 'fio', 'school', 'position',)
    reg_number = forms.CharField(label='Регистрационный номер',
                                 max_length=20,
                                 widget=forms.TextInput(
                                     attrs={'readonly': 'readonly',
                                            'class': 'form-control'}
                                 )
                                 )
    fio = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Участник|Педагог|Коллектив',
        max_length=300)
    school = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Название организации|студии',
        max_length=200)
    position = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-8',
                                      'placeholder': "ученик 3 класса / педагог "}),
        label='Должность|Класс',
        max_length=200)

    status = forms.CharField(widget=forms.HiddenInput, max_length=10)
    year = forms.CharField(widget=forms.HiddenInput, max_length=20)


class ConfirmationUserDataForm(BaseConfirmationUserDataForm):
    level = forms.ChoiceField(label='Класс',
                              choices=Level.objects.all().values_list('id',
                                                                      'name'),
                              )


class ConfirmationUserDataExtraForm(BaseConfirmationUserDataForm):
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Город|Регион',
        max_length=200)
    nomination = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-select col-6'}),
        label='Номинация',
        choices=NominationMYMSK.objects.all().values_list(
            'id',
            'name'))
    author_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Название работы',
        max_length=300)

    teacher = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Руководитель',
        max_length=200)
