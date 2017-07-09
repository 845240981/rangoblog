# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170623_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='views',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
    ]
