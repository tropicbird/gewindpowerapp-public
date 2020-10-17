from django.contrib import admin
from .models import Color, Coordinates, ProjectInfo, Uploadfile

# Register your models here.
admin.site.register(Color)
admin.site.register(Coordinates)
admin.site.register(ProjectInfo)
admin.site.register(Uploadfile)

