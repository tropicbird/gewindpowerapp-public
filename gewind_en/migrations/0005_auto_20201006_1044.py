# Generated by Django 3.1.1 on 2020-10-06 01:44

from django.db import migrations, models
import django.db.models.deletion
import ulid.api.api


class Migration(migrations.Migration):

    dependencies = [
        ('gewind_en', '0004_auto_20201005_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='color',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.PROTECT, to='gewind_en.color', verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=26, primary_key=True, serialize=False),
        ),
    ]
