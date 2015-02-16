from django import forms

from .models import SignUp


class SignUpFormStep1(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['first_name', 'last_name']


class SignUpFormStep2(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email']