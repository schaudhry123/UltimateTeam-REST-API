# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 02:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100, null=True)),
                ('position', models.CharField(max_length=3, null=True)),
                ('nationality', models.CharField(max_length=100, null=True)),
                ('player_league', models.CharField(max_length=100, null=True)),
                ('owner', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='players', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.Team')),
            ],
            options={
                'ordering': ['player_name'],
            },
        ),
    ]
