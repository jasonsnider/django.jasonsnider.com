# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_canonical'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='canonical',
            field=models.CharField(default='', max_length=255),
        ),
    ]
