# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Men'), (2, 'Women'), (3, 'Unisex'), (4, 'Boys'), (5, 'Girls'), (6, 'Kids unisex')], verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='season',
            field=models.IntegerField(choices=[(1, 'Winter'), (2, 'Spring'), (3, 'Summer'), (4, 'Autumn')], verbose_name='Season'),
        ),
    ]
