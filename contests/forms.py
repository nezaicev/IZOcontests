from django import forms
from contests.models import PageContest, Events
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class SubscribeShowEventForm(forms.Form):
    teacher=forms.CharField(max_length=20)
    page_contest=forms.CharField(max_length=20)


class ConfStorageForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.TextInput)
    container = forms.CharField(widget=forms.TextInput)


class PageContestsFrom(forms.ModelForm):
    name = forms.CharField(label='Название')
    logo = forms.ImageField(label='Логотип')
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')
    letter = forms.CharField(widget=CKEditorUploadingWidget(), label='Информационное письмо')

    class Meta:
        fields = ('hide','name', 'logo','type', 'content','letter', 'start_date')
        model = PageContest


def get_my_choices(model, field):
    choices_list = tuple((i, i) for i in
                         model.objects.filter(field=field,access=True).values_list('data',
                                                                       flat=True))
    return choices_list





# class MymoskvichiForm(forms.ModelForm):
#     model = Mymoskvichi
#
#     def __init__(self, *args, **kwargs):
#         super(MymoskvichiForm, self).__init__(*args, **kwargs)
#         self.fields['nomination'] = forms.ChoiceField(label='Номинация',
#                                                       choices=get_my_choices(
#                                                           MymoskvichiSelect,
#                                                           'nomination'))
#         self.fields['nomination_extra'] = forms.ChoiceField(label='Доп. номинация',
#                                                             choices=get_my_choices(
#                                                                 MymoskvichiSelect,
#                                                                 'nomination'))
#         self.fields['age'] = forms.ChoiceField(label='Возрастная категория',
#             choices=get_my_choices(MymoskvichiSelect, 'age'))
#
#

