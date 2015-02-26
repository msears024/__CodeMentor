from django.db import models
from django.utils.encoding import smart_unicode
from django.core.exceptions import ValidationError

# Create your models here.

class SignUp(models.Model):
    first_name = models.CharField(max_length=120, blank=True)
    last_name = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.email)

class ContactUs(models.Model):
    first_name = models.CharField(max_length=120, null=False, blank=True)
    last_name = models.CharField(max_length=120, null=False, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.email)


class VenueRegistration(models.Model):
    venue_name = models.CharField(max_length=120, null=False, blank=False)

    mng_first_name = models.CharField(max_length=120, blank=False)
    mng_last_name = models.CharField(max_length=120, blank=False)
    event_url = models.URLField()
    
    venue_phone = models.CharField(max_length=10, null=True, blank=False)
    main_venue_addy = models.CharField(max_length=120, null=True, blank=False)
    secondary_venue_addy = models.CharField(max_length=120, null=True, blank=False)
    venue_city = models.CharField(max_length=90, null=True, blank=False)
    venue_zip = models.CharField(max_length=5, null=True, blank=False)

    venue_fb = models.CharField(max_length=120, null=True, blank=True)
    venue_twitter = models.CharField(max_length=120, null=True, blank=True)
    venue_yelp = models.CharField(max_length=120, null=True, blank=True)

class EventCategory(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    event_title = models.CharField(max_length=120, null=True, blank=False)
    event_description = models.TextField()
    event_date = models.DateField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()

    event_venue = models.CharField(max_length=120, null=True, blank=False)
    event_category = models.ForeignKey(EventCategory)
    main_event_addy = models.CharField(max_length=120, null=True, blank=False)
    secondary_event_addy = models.CharField(max_length=120, null=True, blank=True)
    event_addy_city = models.CharField(max_length=90, null=True, blank=False)
    event_addy_zip = models.CharField(max_length=5, null=True, blank=False)
    


    def clean(self):
        if self.event_title != "abc":
            raise ValidationError({'event_title':'This can only by abc!'})
        else:
            pass




