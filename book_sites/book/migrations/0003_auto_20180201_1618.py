# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-01 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20180201_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='book_translator',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
