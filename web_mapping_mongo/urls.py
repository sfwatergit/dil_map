from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import mongo_leaflet
from web_mapping_mongo import settings


urlpatterns = patterns('',
    # Examples`:
    # url(r'^web_mapping_mongo/', include('web_mapping_mongo.foo.urls')),
    url(r'^map/', include('mongo_leaflet.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),



)
# if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns += patterns('',
    #                         url(r'^__debug__/', include(debug_toolbar.urls)),

