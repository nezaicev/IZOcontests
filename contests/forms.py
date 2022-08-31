from django import forms
from contests.models import PageContest, Events, CreativeTack
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class InputFile(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    data_file=forms.FileField(widget=forms.FileInput)


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
    alias = forms.CharField(label='Псевдоним')
    email = forms.EmailField(label='Email')
    logo = forms.ImageField(label='Логотип')
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')
    letter = forms.CharField(widget=CKEditorUploadingWidget(), label='Информационное письмо')

    class Meta:
        fields = ('hide','name','alias', 'email','logo','type', 'content','letter', 'start_date', )
        model = PageContest


class CreativeTackAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(),
                              label='Контент')

    class Meta:
        fields= ('contest_name', 'year_contest', 'theme')
        model= CreativeTack





def get_my_choices(model, field):
    choices_list = tuple((i, i) for i in
                         model.objects.filter(field=field,access=True).values_list('data',
                                                                       flat=True))
    return choices_list





