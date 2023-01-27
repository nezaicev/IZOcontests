from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from content.models import Page
from ckeditor.widgets import CKEditorWidget

class ContentCreateForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorWidget(),
        )

    class Meta:
        fields = '__all__'
        model = Page