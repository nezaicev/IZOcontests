from django import forms


class UploadXlsFrom(forms.Form):
    file = forms.FileField(widget=forms.FileInput)