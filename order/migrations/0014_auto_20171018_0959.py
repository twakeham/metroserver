# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 22:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20171018_0906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='flag',
            new_name='booked',
        ),
    ]
