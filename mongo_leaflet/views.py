# Create your views here.
import json

from djgeojson.views import GeoJSONLayerView


from mongo_leaflet.models import DILProject




class MapLayer(GeoJSONLayerView):
    model = DILProject


    properties = (
        'project_name',
        'research_group',
        'department',
        'website',
        'e_mail',
        'partner_org',
        'notes',
        'affiliation',
        'slug',
    )