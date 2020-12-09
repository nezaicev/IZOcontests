from django import forms
from contests.models import  PageContest
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PageContestsFrom(forms.ModelForm):
    name=forms.CharField()
    logo=forms.ImageField()
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        fields = ('name', 'logo','content')
        model = PageContest
