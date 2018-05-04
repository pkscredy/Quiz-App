# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-01 22:33
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quiz_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
