# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0002_auto_20171018_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='canceled',
            field=models.NullBooleanField(default=False),
        ),
    ]