# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-01 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='exam',
            new_name='quiz',
        ),
    ]
