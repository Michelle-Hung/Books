# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-07 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0021_auto_20180307_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='catalog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Catalog'),
        ),
    ]
