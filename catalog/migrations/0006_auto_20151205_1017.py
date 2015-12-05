# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


def prepopulate_options(apps, schema_editor):
    Option = apps.get_model("catalog", "Option")
    for option in settings.DYNAMIC_OPTIONS:
        Option.objects.create(key=option)


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_option'),
    ]

    operations = [
        migrations.RunPython(prepopulate_options),
    ]
