# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-04-08 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180407_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='loginscu',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
