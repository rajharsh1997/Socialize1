# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20170726_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User'),
        ),
    ]
