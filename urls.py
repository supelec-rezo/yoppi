from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r"^$", "ftp.views.index"),
    url(r"^server/(?P<address>[a-z0-9_.-]+)(?P<path>(/.*)?)$", "ftp.views.server"),
    url(r"^search/$", "ftp.views.search"),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
