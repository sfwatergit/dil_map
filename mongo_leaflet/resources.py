from import_export import resources
from import_export.fields import Field
from models import DILProject

class ProjectResource(resources.ModelResource):


    class Meta:
        model = DILProject
