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


class ConfirmationUserDataEventForm(forms.Form):

    reg_number = forms.CharField(label='Регистрационный номер',
                                     max_length=20,
                                     widget=forms.TextInput(
                                         attrs={'readonly': 'readonly',
                                                'class': 'form-control'}
                                     )
                                     )

    event_name = forms.CharField(label='Название мероприятия',
                                 max_length=200,
                                 widget=forms.TextInput(
                                     attrs={'readonly': 'readonly',
                                            'class': 'form-control'}
                                 )
                                 )

    start_date = forms.CharField(label='Дата',
                                 max_length=30,
                                 widget=forms.TextInput(
                                     attrs={'readonly': 'readonly',
                                            'class': 'form-control'}
                                 )
                                 )


    fio = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Участник',
        max_length=100)
    position = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-8',
                                      'placeholder': "Педагог ИЗО"}),
        label='Должность',
        max_length=100)
    school = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Организация',
        max_length=160)
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Регион|Город',
        max_length=150)


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
        max_length=100)
    position = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-8',
                                      'placeholder': "5-7 лет|3 класс|педагог"}),
        label='Возраст|Класс|Должность',
        max_length=100)
    school = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Название организации|студии',
        max_length=160)
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Город|Регион',
        max_length=150)
    teacher = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Руководитель',
        max_length=110,
        )
    author_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Название работы',
        max_length=120,
        required=False
    )
    owner = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-select col-6'}),
        label='Статус',
        choices=(('Участник','Участник'),('Педагог','Педагог'))

    )

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
        max_length=150)
    nomination = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-select col-6'}),
        label='Номинация',
        choices=NominationMYMSK.objects.all().values_list(
            'id',
            'name'))
    author_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Название работы',
        max_length=120)

    teacher = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}),
        label='Руководитель',
        max_length=110,
        required=False
    )
