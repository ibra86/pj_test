# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-22 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0006_requeststat_is_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requeststat',
            name='is_new',
            field=models.NullBooleanField(),
        ),
    ]
