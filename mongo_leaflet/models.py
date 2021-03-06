import random
from django.db import models
from django.contrib.gis.db import models as gismodels
from django_extensions.db.fields import AutoSlugField
from django.contrib.gis.geos import Point
from django.utils.translation import ugettext_lazy as _
from djgeojson.fields import PointField


class DILProject(models.Model):
    project_name = models.CharField(max_length=200, null=False, blank=False)
    research_group = models.CharField(max_length=200, null=False, blank=True)
    department = models.CharField(max_length=200, null=False, blank=True)
    website = models.URLField(name="website",null=False, blank=True)
    email = models.EmailField(name="email", blank=True, null=False)
    partner_org = models.CharField(max_length=200, blank=True, null=False)
    notes = models.TextField(null=True, blank=True)
    affiliation = models.CharField(max_length=200, null=True)
    geom = PointField()
    slug = AutoSlugField(populate_from='project_name', separator='-')

    def __unicode__(self):
        return self.project_name



