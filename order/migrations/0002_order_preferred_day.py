# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='preferred_day',
            field=models.CharField(default='', max_length=20),
        ),
    ]
