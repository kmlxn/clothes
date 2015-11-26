# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(upload_to='images', verbose_name='Photo')),
                ('gender', models.CharField(choices=[(1, 'Men'), (2, 'Women'), (3, 'Unisex'), (4, 'Boys'), (5, 'Girls'), (6, 'Kids unisex')], verbose_name='Gender/Age', max_length=15)),
                ('season', models.CharField(choices=[(1, 'Winter'), (2, 'Spring'), (3, 'Summer'), (4, 'Autumn')], verbose_name='Season', max_length=15)),
                ('category', models.ForeignKey(verbose_name='Category', to='catalog.Category')),
            ],
            options={
                'verbose_name_plural': 'Clothes',
                'verbose_name': 'Clothing',
            },
        ),
    ]
