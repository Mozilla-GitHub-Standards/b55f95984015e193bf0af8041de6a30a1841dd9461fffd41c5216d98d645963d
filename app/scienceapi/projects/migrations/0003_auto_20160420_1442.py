# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160418_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.BooleanField(default=False, help_text='Has this project been Approved or not'),
        ),
    ]
