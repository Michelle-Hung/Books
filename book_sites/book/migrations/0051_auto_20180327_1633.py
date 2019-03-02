# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-27 08:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0050_auto_20180320_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo_zoom',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='rating',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='書名'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, verbose_name='關於我'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_day',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('女', '女'), ('男', '男'), ('不想回答', '不想回答')], default='F', max_length=1, verbose_name='性別'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='book/media/default.png', upload_to='profile_img', verbose_name='圖片'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='名稱'),
        ),
    ]