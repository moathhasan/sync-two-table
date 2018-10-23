# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-03 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocalVlans',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'local_vlans',
            },
        ),
        migrations.CreateModel(
            name='RemoteVlans',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'remote_vlans',
            },
        ),
        migrations.CreateModel(
            name='tmp',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'tmp',
            },
        ),
    ]
