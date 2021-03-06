# Generated by Django 3.1.1 on 2020-10-05 04:30

from django.db import migrations, models
import ulid.api.api


class Migration(migrations.Migration):

    dependencies = [
        ('gewind_en', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='paint_it_black',
            field=models.BooleanField(default=False, help_text='*Check the box if you want part of the blade to be black.', verbose_name='Birdstrike prevention'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=26, primary_key=True, serialize=False),
        ),
    ]
