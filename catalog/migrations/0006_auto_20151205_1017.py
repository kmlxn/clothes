# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def prepopulate_options(apps, schema_editor):
    Option = apps.get_model("catalog", "Option")
    Option.objects.create(key="about_us_content")
    Option.objects.create(key="phone_number")
    Option.objects.create(key="email")
    Option.objects.create(key="address")


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_option'),
    ]

    operations = [
        migrations.RunPython(prepopulate_options),
    ]
