# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='booked',
            new_name='invoiced',
        ),
        migrations.AddField(
            model_name='run',
            name='manifested',
            field=models.BooleanField(default=False),
        ),
    ]