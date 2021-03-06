# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 15:02
from __future__ import unicode_literals

from django.db import migrations
from django.utils.text import slugify


def create_default_slug(apps, schema_manager):
    Talk = apps.get_model('talk', 'Talk')
    for talk in Talk.objects.all():
        talk.slug = slugify(talk.title)
        talk.save()


class Migration(migrations.Migration):
    dependencies = [
        ('talk', '0029_auto_20181008_1422'),
    ]

    operations = [
        migrations.RunPython(create_default_slug)
    ]
