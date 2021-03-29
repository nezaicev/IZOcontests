from django import forms
from contests.models import Level, Participant, TeacherExtra
from cert.models import Events


class SearchRegNumForm(forms.Form):
    event = forms.ChoiceField(label='Конкурс/мероприятие',
                              choices=Events.objects.all().values_list('id',
                                                                       'name'))
    reg_number = forms.CharField(label='Регистрационный номер', max_length=20)


class BaseConfirmationUserDataForm(forms.Form):
    reg_number = forms.CharField(label='Регистрационный номер',
                                 max_length=20,
                                 widget=forms.TextInput(
                                     attrs={'readonly': 'readonly'}
                                    )
                                 )
    fio = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12'}),
                          label='ФИО для сертификата',
                          max_length=200)
    status = forms.CharField(widget=forms.HiddenInput, max_length=10)


class ConfirmationUserDataForm(BaseConfirmationUserDataForm):
    level = forms.ChoiceField(label='Класс',
                              choices=Level.objects.all().values_list('id',
                                                                      'name'))


class ConfirmationUserDataExtraForm(BaseConfirmationUserDataForm):
    field_order = ("reg_number","fio",)

    fio = forms.CharField(widget=forms.TextInput(attrs={'class':'form control col-6 '}), label='ФИО участника',
                          max_length=200)
    teacher= forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form control col-6'}),
        label='Руководитель',
        max_length=100)
    school = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form control col-8'}),
        label='Название организации/студии',
        max_length=200)




