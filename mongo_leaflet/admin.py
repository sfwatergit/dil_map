from django import forms
from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin
from easy_maps.widgets import AddressWithMapWidget
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from mongo_leaflet.models import DILProject
from mongo_leaflet.resources import ProjectResource
from leaflet.admin import LeafletGeoAdmin

class DILProjectAdmin(ImportExportMixin, LeafletGeoAdmin):
    resource_class = ProjectResource
    pass


admin.site.register(DILProject, DILProjectAdmin)
