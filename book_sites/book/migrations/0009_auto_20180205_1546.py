# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-05 07:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20180205_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2018, 2, 5, 7, 46, 41, 943623, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='book',
            name='synopsis',
            field=models.TextField(null=True),
        ),
    ]