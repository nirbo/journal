# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20170628_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(default='', unique=True)),
                ('netmask', models.GenericIPAddressField(default='')),
                ('vlan', models.CharField(blank=True, max_length=64, null=True)),
                ('data_IP_1', models.GenericIPAddressField(default='', unique=True)),
                ('data_IP_2', models.GenericIPAddressField(blank=True, null=True, unique=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Location')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Owner')),
            ],
        ),
    ]