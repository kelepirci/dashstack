# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-20 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20170420_1457'),
        ('role', '0020_auto_20170420_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='target',
            new_name='target_domain',
        ),
        migrations.AddField(
            model_name='assignment',
            name='target_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
    ]