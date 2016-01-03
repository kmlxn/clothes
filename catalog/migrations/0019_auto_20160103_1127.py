# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_auto_20151231_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='comment',
            field=models.CharField(verbose_name='Comment', null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='option',
            name='comment_en',
            field=models.CharField(verbose_name='Comment', null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='option',
            name='comment_ru',
            field=models.CharField(verbose_name='Comment', null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='option',
            name='comment_uz',
            field=models.CharField(verbose_name='Comment', null=True, blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='option',
            name='value',
            field=models.CharField(verbose_name='Value', null=True, blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='option',
            name='value_en',
            field=models.CharField(verbose_name='Value', null=True, blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='option',
            name='value_ru',
            field=models.CharField(verbose_name='Value', null=True, blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='option',
            name='value_uz',
            field=models.CharField(verbose_name='Value', null=True, blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_text',
            field=models.TextField(verbose_name='Order Text'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Order Time'),
        ),
    ]
