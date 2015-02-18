from django.contrib import admin

# Register your models here.
from .models import *

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp

class ContactUsAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactUs


admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(SignUp, SignUpAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
