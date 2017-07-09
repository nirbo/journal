# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='bmc_IP',
            field=models.GenericIPAddressField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='data_IP_1',
            field=models.GenericIPAddressField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='data_IP_2',
            field=models.GenericIPAddressField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='mgmt_IP',
            field=models.GenericIPAddressField(default='', unique=True),
        ),
    ]