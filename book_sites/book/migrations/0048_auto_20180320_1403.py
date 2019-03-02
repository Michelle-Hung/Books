# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-20 06:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0047_auto_20180320_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='書名'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='book/media/profile_img/default.png', upload_to='profile_img'),
        ),
    ]
