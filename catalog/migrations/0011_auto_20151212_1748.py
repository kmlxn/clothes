# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20151212_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_uz',
            field=models.TextField(verbose_name='Description', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uz',
            field=models.CharField(verbose_name='Title', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='url_name_uz',
            field=models.CharField(verbose_name='Url Name', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clothing',
            name='description_uz',
            field=models.TextField(verbose_name='Description', null=True),
        ),
        migrations.AddField(
            model_name='clothing',
            name='title_uz',
            field=models.CharField(verbose_name='Title', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='option',
            name='value_uz',
            field=models.CharField(verbose_name='Value', max_length=255, null=True),
        ),
    ]
