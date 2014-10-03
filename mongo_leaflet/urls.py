from django.conf.urls import patterns, url
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.views.generic import TemplateView

from mongo_leaflet.models import DILProject
from mongo_leaflet.views import MapLayer


urlpatterns = patterns("",
                       url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),


                       url(r'^data.geojson$', MapLayer.as_view(), name='data'),

)


