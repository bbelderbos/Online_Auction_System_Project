# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 02:56
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_system', '0002_auto_20160727_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidder',
            name='bid_amount',
            field=models.CharField(default=100, max_length=255, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numerics are allowed.')]),
            preserve_default=False,
        ),
    ]
