# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-16 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0033_auto_20180316_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='讚'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='書名'),
        ),
    ]
