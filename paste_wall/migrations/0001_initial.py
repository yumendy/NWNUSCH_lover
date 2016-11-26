# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('class_num', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('author', models.CharField(blank=True, max_length=64, null=True)),
                ('is_anonymous', models.BooleanField(default=True)),
                ('is_checked', models.BooleanField(default=False)),
                ('author_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
    ]
