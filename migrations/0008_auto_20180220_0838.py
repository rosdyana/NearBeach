# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-19 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0007_auto_20180217_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='organisations_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NearBeach.organisations'),
        ),
    ]