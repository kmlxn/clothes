# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20151214_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='season',
            field=models.IntegerField(choices=[(1, 'Winter'), (2, 'Spring'), (3, 'Summer'), (4, 'Autumn'), (5, 'Uni'), (6, 'Autumn/Winter'), (7, 'Spring/Summer')], verbose_name='Season'),
        ),
    ]
