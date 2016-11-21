# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Strip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
                ('alt', models.CharField(max_length=500)),
                ('subtext', models.CharField(max_length=100000)),
            ],
        ),
    ]
