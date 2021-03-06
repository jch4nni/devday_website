# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0028_add_slugs_to_talks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talkformat',
            options={'verbose_name': 'Talk Format', 'verbose_name_plural': 'Talk Format'},
        ),
        migrations.AlterField(
            model_name='talk',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Slug'),
        ),
        migrations.AlterUniqueTogether(
            name='talkformat',
            unique_together=set([('name', 'duration')]),
        ),
    ]
