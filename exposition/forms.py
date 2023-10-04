from django.forms import ModelForm
from file_resubmit.admin import AdminResubmitImageWidget, AdminResubmitFileWidget
from exposition.models import Exposition


class PageModelForm(ModelForm):

    class Meta:
        fields = '__all__'
        model = Exposition
        widgets = {
            'picture': AdminResubmitImageWidget,
            'file': AdminResubmitFileWidget,
        }