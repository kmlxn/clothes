# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20151229_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 12, 31, 1, 30, 38, 973796, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
