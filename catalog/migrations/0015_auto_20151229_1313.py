# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20151229_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client_company',
            field=models.CharField(max_length=255, null=True, verbose_name='Client Company', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='client_phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], max_length=255, null=True, verbose_name='Client Phone', blank=True),
        ),
    ]
