# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0006_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='owner',
            new_name='username',
        ),
    ]