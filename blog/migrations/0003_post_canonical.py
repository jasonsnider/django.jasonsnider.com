# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170113_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='canonical',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
