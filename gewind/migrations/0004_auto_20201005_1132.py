# Generated by Django 3.1.1 on 2020-10-05 02:32

from django.db import migrations, models
import ulid.api.api


class Migration(migrations.Migration):

    dependencies = [
        ('gewind', '0003_auto_20201005_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=26, primary_key=True, serialize=False),
        ),
    ]