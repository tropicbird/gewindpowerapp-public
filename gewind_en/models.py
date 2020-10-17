from django.db import models
import ulid

# Create your models here.

class Color(models.Model):
    color=models.CharField('Color',max_length=255,unique=True)
    def __str__(self):
        return self.color

class ProjectInfo(models.Model):
    id=models.CharField(
        default=ulid.new,
        max_length=26,
        primary_key=True,
        editable=False
    )

    proj_id = models.CharField('Project Name', max_length=255, unique=False)
    color = models.ForeignKey(Color, on_delete=models.PROTECT, verbose_name='Color',default=8)
    heading=models.IntegerField('Heading (0 to 360)',default=0,help_text='*North = 0, East = 90, South = 180, West = 270')
    hub_height=models.FloatField('Hub height (m)',default=100)
    blade_length=models.FloatField('Blade length (m)',default=80,help_text='*It is a rotor radius, NOT a rotor diameter.')
    created_at=models.DateTimeField('Created',auto_now_add=True)
    updated_at=models.DateTimeField('Updated',auto_now=True)
    appearance = models.BooleanField('Position of the blade',help_text='*Check the box if you want the blade rotation position to be random.')
    paint_it_black = models.BooleanField('Birdstrike prevention', help_text='*Check the box if you want part of the blade to be black.', default=False)  # 10/05

    def __str__(self):
        return self.proj_id

class Coordinates(models.Model):
    turbine_name=models.CharField('Wind turbine name',max_length=32,blank=True,help_text='a')
    lon=models.FloatField('Longitude',help_text='a',blank=False)
    lat = models.FloatField('Latitude',help_text='a',blank=False)
    export_id = models.ForeignKey(ProjectInfo, on_delete=models.PROTECT, verbose_name='export_id')

    def __str__(self):
        return self.turbine_name

class Uploadfile(models.Model):
    file = models.FileField('File')
    name = models.CharField('Name of the file',max_length=32,blank=True)

    def __str__(self):
        return self.file.url