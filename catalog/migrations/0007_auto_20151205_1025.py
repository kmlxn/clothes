# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20151205_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='key_en',
            field=models.CharField(verbose_name='Key', null=True, max_length=255),
        ),
        migrations.AddField(
            model_name='option',
            name='key_ru',
            field=models.CharField(verbose_name='Key', null=True, max_length=255),
        ),
        migrations.AddField(
            model_name='option',
            name='value_en',
            field=models.CharField(verbose_name='Value', null=True, max_length=255),
        ),
        migrations.AddField(
            model_name='option',
            name='value_ru',
            field=models.CharField(verbose_name='Value', null=True, max_length=255),
        ),
    ]
