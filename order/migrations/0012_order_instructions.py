# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20171016_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='instructions',
            field=models.TextField(null=True),
        ),
    ]
