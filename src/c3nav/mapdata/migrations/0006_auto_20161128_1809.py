# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 18:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0005_auto_20161128_1735'),
    ]

    operations = [
        migrations.RenameModel('Area', 'Room')
    ]