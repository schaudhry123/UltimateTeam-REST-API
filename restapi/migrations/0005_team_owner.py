# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0004_auto_20160422_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='owner',
            field=models.CharField(max_length=100, null=True),
        ),
    ]