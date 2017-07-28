# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 04:58
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('searchlist', '0010_auto_20170728_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='city',
            field=models.CharField(default=b'Seattle', max_length=128),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='resource',
            name='org_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resource',
            name='state',
            field=localflavor.us.models.USStateField(default=b'Washington', max_length=2),
        ),
        migrations.AlterField(
            model_name='resource',
            name='street',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='zip_code',
            field=localflavor.us.models.USZipCodeField(blank=True, max_length=10, null=True),
        ),
    ]
