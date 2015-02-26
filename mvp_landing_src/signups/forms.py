from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView

from crispy_forms.helper import FormHelper

from .models import (SignUp, ContactUs as contactus, Event,
                      VenueRegistration, EventCategory,)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp

class UserRegistration(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.form_method = "POST"
    def clean(self):
        p1 = self.cleaned_data.get('password1', None)
        p2 = self.cleaned_data.get('password2', None)
        username = self.cleaned_data.get('username', None)
        if p1 is not None and p2 is not None:
            if p1 != p2:
                self.add_error("password1", "Passwords do not match.")
        if username is not None:
            if User.objects.filter(username=username).exists():
                self.add_error("username", "Username already exists.")

    # def as_h(self):
    #     return "<h1>Hellow world</h1>"

class ContactUs(forms.ModelForm):
    class Meta:
        model = contactus

class VenueRegistrationOne(forms.ModelForm):
    pass

class VenueRegistrationTwo(forms.Form):
    pass

class VenueRegistrationThree(forms.Form):
    pass

class EventOne(forms.Form):
    event_title = forms.CharField()
    event_description = forms.CharField()
    event_date = forms.DateField()
    event_start_time = forms.TimeField()
    event_end_time = forms.TimeField()

class EventTwo(forms.Form):
    event_venue = forms.CharField()
    event_category = forms.ModelChoiceField(queryset=EventCategory.objects.all())
    main_event_addy = forms.CharField()
    secondary_event_addy = forms.CharField()
    event_addy_city = forms.CharField()
    event_addy_zip = forms.CharField()

class EventWizard(SessionWizardView):
    def done(self, form_list, **kwargs):
        return render_to_response('registration.html', {
            'form_data': [form.cleaned_data for form in form_list],
            })


