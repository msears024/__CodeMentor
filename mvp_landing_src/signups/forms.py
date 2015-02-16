from django import forms

from .models import SignUp, ContactUs as contactus 

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp

class ContactUs(forms.ModelForm):
    class Meta:
        model = contactus

class VenueRegistration():
    pass


