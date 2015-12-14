# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20151212_1748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'verbose_name': 'Option', 'verbose_name_plural': 'Options'},
        ),
        migrations.AlterField(
            model_name='clothing',
            name='description',
            field=models.TextField(verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='description_en',
            field=models.TextField(verbose_name='Description', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='description_ru',
            field=models.TextField(verbose_name='Description', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='description_uz',
            field=models.TextField(verbose_name='Description', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='season',
            field=models.IntegerField(verbose_name='Season', choices=[(1, 'Winter'), (2, 'Spring'), (3, 'Summer'), (4, 'Autumn'), (4, 'Uni'), (4, 'Autumn/Winter'), (4, 'Spring/Summer')]),
        ),
    ]
