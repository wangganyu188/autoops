# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product_line',
            new_name='product_lines',
        ),
        migrations.AlterModelTable(
            name='product_lines',
            table=' product_lines',
        ),
    ]