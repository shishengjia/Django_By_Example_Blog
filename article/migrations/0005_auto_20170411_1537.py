# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-11 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_remove_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='article.Tag'),
        ),
    ]
