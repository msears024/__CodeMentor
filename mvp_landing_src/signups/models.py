from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.email)

class ContactUs(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.email)

class VenueRegistration(models.Model):
    venue_name = models.CharField(max_length=120, null=True, blank=False)

    mng_first_name = models.CharField(max_length=120, null=True, blank=False)
    mng_last_name = models.CharField(max_length=120, null=True, blank=False)
    event_url = forms.URLField(label='Venue URL:', required=True)
    
    venue_phone = CharField(max_length=10, null=True, blank=False)
    main_venue_addy = models.CharField(max_length=120, null=True, blank=False)
    secondary_venue_addy = models.CharField(max_length=120, null=True, blank=False)
    venue_city = models.CharField(max_length=90, null=True, blank=False)
    venue_zip = models.CharField(max_length=5, null=True, blank=False)

    venue_fb = models.CharField(max_length=120, null=True, blank=True)
    venue_twitter = models.CharField(max_length=120, null=True, blank=True)
    venue_yelp = models.CharField(max_length=120, null=True, blank=True)

class Event(models.model):
    event_venue = models.CharField(max_length=120, null=True, blank=False)
    event_title = models.CharField(max_length=120, null=True, blank=False)

    # event_category = 
    main_event_addy = models.CharField(max_length=120, null=True, blank=False)
    secondary_event_addy = models.CharField(max_length=120, null=True, blank=False)
    event_addy_city = models.CharField(max_length=90, null=True, blank=False)
    event_addy_zip = models.CharField(max_length=5, null=True, blank=False)

    




