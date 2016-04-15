# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0006_auto_20160414_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=b'', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='restapi.Team'),
        ),
    ]
