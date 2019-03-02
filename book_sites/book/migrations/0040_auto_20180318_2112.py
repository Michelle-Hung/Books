# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-18 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0039_auto_20180318_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='書名'),
        ),
    ]
