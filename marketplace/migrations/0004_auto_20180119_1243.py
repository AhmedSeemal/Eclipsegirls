# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-19 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_auto_20180119_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplace',
            name='product_image',
            field=models.ImageField(upload_to='', verbose_name='Upload Image'),
        ),
    ]
