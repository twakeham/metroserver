# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('meterage', models.IntegerField()),
            ],
        ),
    ]
