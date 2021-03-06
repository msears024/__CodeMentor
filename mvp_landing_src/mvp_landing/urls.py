from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
    url(r'^contact-us/$', 'signups.views.contactus', name='contactus'),
    url(r'^get-started/$', 'signups.views.getstarted', name='getstarted'),
    url(r'^upload-event/$', 'signups.views.uploadevent', name='uploadevent'),
    
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)


