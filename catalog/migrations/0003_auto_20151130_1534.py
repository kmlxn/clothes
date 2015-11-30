# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20151125_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(verbose_name='Description', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(verbose_name='Description', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name='Title', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=255, verbose_name='Title', null=True),
        ),
        migrations.AddField(
            model_name='clothing',
            name='description_en',
            field=models.TextField(verbose_name='Description', null=True),
        ),
        migrations.AddField(
            model_name='clothing',
            name='description_ru',
            field=models.TextField(verbose_name='Description', null=True),
        ),
        migrations.AddField(
            model_name='clothing',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name='Title', null=True),
        ),
        migrations.AddField(
            model_name='clothing',
            name='title_ru',
            field=models.CharField(max_length=255, verbose_name='Title', null=True),
        ),
    ]
