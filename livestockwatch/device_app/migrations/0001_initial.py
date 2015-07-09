# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date_modified')),
                ('name', models.CharField(max_length=20, verbose_name='Name', unique=True)),
                ('stall', models.OneToOneField(to='farm_app.Stall')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date_modified')),
                ('cpu_usage', models.FloatField(null=True, verbose_name='Cpu usage')),
                ('disk_usage', models.FloatField(null=True, verbose_name='Disk usage')),
                ('memory_usage', models.FloatField(null=True, verbose_name='Memory usage')),
                ('time_taken', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time taken')),
                ('device', models.ForeignKey(to='device_app.Device')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date_modified')),
                ('severity', models.IntegerField(choices=[(1, 'Critical error'), (0, 'Warning')], null=True, verbose_name='Severity')),
                ('component', models.IntegerField(choices=[(0, 'Camera'), (1, 'ADDA board'), (2, 'Network')], null=True, verbose_name='Component')),
                ('status', models.IntegerField(choices=[(1, 'Resolved'), (0, 'Unresolved')], verbose_name='Status', default=0)),
                ('message', models.TextField(null=True, verbose_name='Message')),
                ('time_taken', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time taken')),
                ('device', models.ForeignKey(to='device_app.Device')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date_modified')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('remarks', models.TextField(null=True, verbose_name='Remarks')),
                ('time_taken', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time taken')),
                ('device', models.ForeignKey(to='device_app.Device')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='devicelog',
            unique_together=set([('device', 'time_taken')]),
        ),
        migrations.AlterUniqueTogether(
            name='devicecondition',
            unique_together=set([('device', 'time_taken')]),
        ),
    ]
