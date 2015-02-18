from django import forms

from .models import (SignUp, ContactUs as contactus, Event,
                      VenueRegistration, EventCategory)

from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp

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


