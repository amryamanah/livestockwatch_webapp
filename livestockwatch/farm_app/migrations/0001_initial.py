# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('name', models.CharField(verbose_name='Place Name', unique=True, max_length=30)),
                ('address', models.TextField(max_length=300, verbose_name='Place Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stall',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('name', models.CharField(verbose_name='Stall Name', default='', unique=True, blank=True, max_length=30)),
                ('remarks', models.CharField(max_length=60, default='', verbose_name='Remarks', blank=True)),
                ('head_count', models.IntegerField(verbose_name='Head count', null=True)),
                ('place', models.ForeignKey(to='farm_app.Place')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
