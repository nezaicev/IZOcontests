from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser


class UraoUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser

        fields = ('email', 'fio',
                  'school', 'region',
                  'phone', 'status',
                'password1', 'password2',
                  )
        widgets = {
            # 'status': forms.Select(attrs={'class': 'form-select',
            #                               'onchange': 'hideAdditionalInfo(this)',
            #                               'initial': 4,
            #                               }),

            'status': forms.HiddenInput(attrs={'value': 4}),

            'email': forms.TextInput(attrs={'class': 'form-control ',
                                            'type': 'email',
                                            'placeholder': 'name@example.com',
                                            'id': 'exampleFormControlInput1',
                                            }),
            'fio': forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Иванов Иван Иванович'}),
            'region': forms.Select(attrs={'class': 'form-select',
                                          'onchange': 'regionChanged(this)',
                                          'initial': 1}),
            'district': forms.Select(attrs={'class': 'form-select', }),
            'city': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'school': forms.HiddenInput(attrs={'value': 'УРАО'}),

            'phone': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].initial = 4

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
