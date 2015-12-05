# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20151205_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='value',
            field=models.CharField(max_length=255, verbose_name='Value', null=True),
        ),
    ]
