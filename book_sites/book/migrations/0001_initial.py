# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-01 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_no', models.IntegerField()),
                ('catalog', models.CharField(max_length=25)),
                ('book_name', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
