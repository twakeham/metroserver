# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20171015_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='flags',
            name='acknowledged',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
