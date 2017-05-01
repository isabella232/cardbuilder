# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170413_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='authors',
        ),
        migrations.AddField(
            model_name='card',
            name='copyedited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='card',
            name='production_notes',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]