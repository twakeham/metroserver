# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 02:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suburb',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='suburb',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suburb.Zone'),
        ),
    ]
