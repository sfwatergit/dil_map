from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import mongo_leaflet
from django.conf import global_settings

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Examples`:

    # url(r'^web_mapping_mongo/', include('web_mapping_mongo.foo.urls')),
    url(r'^map/', include('mongo_leaflet.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),



)


