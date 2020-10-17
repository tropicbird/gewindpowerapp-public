# Generated by Django 3.1.1 on 2020-10-05 02:32

from django.db import migrations, models
import ulid.api.api


class Migration(migrations.Migration):

    dependencies = [
        ('gewind', '0002_auto_20201005_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='paint_it_black',
            field=models.BooleanField(default=False, help_text='※ブレードの一部を黒くする場合はチェックを入れる。', verbose_name='バードストライク対策'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=26, primary_key=True, serialize=False),
        ),
    ]
