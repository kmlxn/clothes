# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 31, 1, 35, 21, 406280, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
