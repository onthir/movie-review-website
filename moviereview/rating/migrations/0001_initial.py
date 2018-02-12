# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-11 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
                ('director', models.CharField(max_length=150)),
                ('cast', models.CharField(max_length=250)),
                ('image', models.URLField(max_length=1000)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]