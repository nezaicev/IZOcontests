from django import forms
from contests.models import PageContest, Mymoskvichi, MymoskvichiSelect
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ConfStorageForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.TextInput)
    container = forms.CharField(widget=forms.TextInput)


class PageContestsFrom(forms.ModelForm):
    name = forms.CharField()
    logo = forms.ImageField()
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        fields = ('name', 'logo', 'content')
        model = PageContest


def get_my_choices(model, field):
    choices_list = tuple((i, i) for i in
                         model.objects.filter(field=field).values_list('data',
                                                                       flat=True))
    return choices_list


class MymoskvichiForm(forms.ModelForm):
    model = Mymoskvichi

    def __init__(self, *args, **kwargs):
        super(MymoskvichiForm, self).__init__(*args, **kwargs)
        self.fields['nomination'] = forms.ChoiceField(label='Номинация',
                                                      choices=get_my_choices(
                                                          MymoskvichiSelect,
                                                          'nomination'))
        self.fields['nomination_extra'] = forms.ChoiceField(label='Доп. номинация',
                                                            choices=get_my_choices(
                                                                MymoskvichiSelect,
                                                                'nomination'))
        self.fields['age'] = forms.ChoiceField(label='Возрастная категория',
            choices=get_my_choices(MymoskvichiSelect, 'age'))
