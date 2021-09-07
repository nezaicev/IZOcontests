from django import forms
from contests.models import Level, Participant, TeacherExtra
from contests.directory import NominationMYMSK
from contests.models import Events
from django.forms.widgets import ChoiceWidget, Input
from django.contrib import messages


class SearchRegNumForm(forms.Form):

    event = forms.ChoiceField(label='Конкурс/мероприятие',

                              )
    reg_number = forms.CharField(label='Регистрационный номер', max_length=20)

    # class Meta:
    #     fields = ('reg_number','event')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the query here
        MYQUERY = Events.objects.all().values_list('id','name')
        self.fields['event'] = forms.ChoiceField(choices=(*MYQUERY,),label='Конкурс/мероприятие')


class BaseConfirmationUserDataForm(forms.Form):
    field_order = ('reg_number', 'fio', 'position', 'school')
    reg_number = forms.CharField(label='Регистрационный номер',
                                 max_length=20,
                                 widget=forms.TextInput(
                                     attrs={'readonly': 'readonly'}
                                 )
                                 )
    fio = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-6'}),
                          label='ФИО участника',
                          max_length=200)
    position = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-6',
                                                             'placeholder': "ученик 3 класса / педагог "}),
                               label='Должность/класс',
                               max_length=200)
    school = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form control col-8'}),
        label='Название организации/студии',
        max_length=200)

    status = forms.CharField(widget=forms.HiddenInput, max_length=10)


class ConfirmationUserDataForm(BaseConfirmationUserDataForm):
    level = forms.ChoiceField(label='Класс',
                              choices=Level.objects.all().values_list('id',
                                                                      'name'))


class ConfirmationUserDataExtraForm(BaseConfirmationUserDataForm):
    nomination = forms.ChoiceField(label='Номинация',
                                   choices=NominationMYMSK.objects.all().values_list(
                                       'id',
                                       'name'))
