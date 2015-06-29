# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cattle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('id_number', models.CharField(verbose_name='id_number', unique=True, max_length=12)),
                ('regist_num_father', models.CharField(verbose_name='regist_num_father', max_length=12)),
                ('regist_num_mother', models.CharField(verbose_name='regist_num_mother', max_length=12)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('CM', 'Castrated Male')], default='F', verbose_name='sex', max_length=2)),
                ('birthday', models.DateField(null=True, verbose_name='birthday', blank=True)),
                ('fat_start_date', models.DateField(null=True, verbose_name='fat_start_date', blank=True)),
                ('fat_finish_date', models.DateField(null=True, verbose_name='fat_finish_date', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CattleNeckband',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('is_active', models.BooleanField(verbose_name='is_active', default=False)),
                ('start_date', models.DateField(null=True, verbose_name='start_date', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name='end_date', blank=True)),
                ('cattle', models.ForeignKey(to='core_app.Cattle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NeckbandPattern',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('pattern', models.CharField(verbose_name='pattern', unique=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('name', models.CharField(verbose_name='Place Name', unique=True, max_length=30)),
                ('address', models.TextField(verbose_name='Place Address', max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stall',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('device_name', models.CharField(verbose_name='Stall Device Name', unique=True, max_length=30)),
                ('name', models.CharField(blank=True, default='', verbose_name='Stall Name', unique=True, max_length=30)),
                ('remarks', models.CharField(blank=True, default='', verbose_name='remarks', max_length=60)),
                ('head_count', models.IntegerField(null=True, verbose_name='head_count')),
                ('place', models.ForeignKey(to='core_app.Place')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cattleneckband',
            name='neckband_pattern',
            field=models.ForeignKey(to='core_app.NeckbandPattern'),
        ),
        migrations.AddField(
            model_name='cattle',
            name='stall',
            field=models.ForeignKey(to='core_app.Stall'),
        ),
    ]
