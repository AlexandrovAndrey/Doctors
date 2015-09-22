# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(verbose_name='date published')),
                ('doctor_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(verbose_name='date published')),
                ('entry_time', models.TimeField(verbose_name='entry time')),
                ('entry_date', models.DateField(verbose_name='entry date')),
                ('client_name', models.CharField(max_length=200)),
                ('doctor_name', models.ForeignKey(to='entries.Doctors')),
            ],
        ),
    ]
