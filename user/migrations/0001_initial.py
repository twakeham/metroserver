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
            name='Permissions',
            fields=[
                ('code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('super_user', models.BooleanField(default=False)),
                ('permissions', models.ManyToManyField(to='user.Permissions')),
            ],
        ),
    ]
