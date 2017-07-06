# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-05 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20170526_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_virtual',
            field=models.BooleanField(default=False, help_text="When selected, events will appear on site converted to a visitor's local time.", verbose_name='Virtual Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='timezone',
            field=models.CharField(default='UTC', help_text='Timezone of the place where the event will be held. If the event is virtual, use whatever time zone you like and enter the times in that zone.', max_length=40),
            preserve_default=False,
        ),
    ]