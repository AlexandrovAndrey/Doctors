# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_worktime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='entry_time',
            field=models.CharField(max_length=200),
        ),
    ]
