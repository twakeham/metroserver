# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20171018_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoiced',
            field=models.NullBooleanField(default=True),
        ),
    ]
