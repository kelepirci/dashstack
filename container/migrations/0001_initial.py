# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-18 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField()),
                ('deleted', models.BooleanField(default=False)),
                ('project_id', models.CharField(max_length=255)),
                ('resource', models.CharField(max_length=255)),
                ('hard_limit', models.IntegerField(max_length=11)),
            ],
        ),
    ]