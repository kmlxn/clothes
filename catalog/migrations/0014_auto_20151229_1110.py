# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20151214_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('client_name', models.CharField(max_length=255, verbose_name='Client Name')),
                ('client_email', models.EmailField(max_length=255, verbose_name='Client Email')),
                ('client_company', models.CharField(max_length=255, verbose_name='Client Company', null=True)),
                ('client_phone', models.CharField(max_length=255, verbose_name='Client Phone', null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('order_text', models.TextField(verbose_name='Order text')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.AlterField(
            model_name='clothing',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Men'), (2, 'Women'), (3, 'Unisex'), (4, 'Boys'), (5, 'Girls'), (6, 'Kids unisex')], verbose_name='Gender/Age'),
        ),
    ]
