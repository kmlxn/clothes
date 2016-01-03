# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_auto_20160103_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='value',
            field=models.TextField(null=True, verbose_name='Value', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='option',
            name='value_en',
            field=models.TextField(null=True, verbose_name='Value', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='option',
            name='value_ru',
            field=models.TextField(null=True, verbose_name='Value', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='option',
            name='value_uz',
            field=models.TextField(null=True, verbose_name='Value', blank=True, max_length=255),
        ),
    ]
