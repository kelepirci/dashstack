# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-20 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0002_auto_20170420_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='type',
            field=models.IntegerField(choices=[(1, 'UserProject'), (2, 'GroupProject'), (3, 'UserDomain'), (4, 'GroupDomain')]),
        ),
    ]
