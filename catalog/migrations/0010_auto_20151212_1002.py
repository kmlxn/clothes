# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20151205_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url_name',
            field=models.CharField(default='jeans', verbose_name='Url Name', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='url_name_en',
            field=models.CharField(null=True, verbose_name='Url Name', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='url_name_ru',
            field=models.CharField(null=True, verbose_name='Url Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='option',
            name='key',
            field=models.CharField(verbose_name='Key', unique=True, max_length=255),
        ),
    ]
