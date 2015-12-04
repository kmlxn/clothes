# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20151130_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='images', verbose_name='Photo'),
        ),
    ]
