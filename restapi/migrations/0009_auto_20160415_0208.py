# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0008_auto_20160415_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]