# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageanalysisparameter',
            name='parameter',
        ),
        migrations.AddField(
            model_name='imageanalysisparameter',
            name='hue_max',
            field=models.FloatField(default=1.0, verbose_name='Hue threshold max'),
        ),
        migrations.AddField(
            model_name='imageanalysisparameter',
            name='hue_min',
            field=models.FloatField(default=0.0, verbose_name='Hue threshold min'),
        ),
        migrations.AddField(
            model_name='imageanalysisparameter',
            name='sat_max',
            field=models.FloatField(default=1.0, verbose_name='Saturation threshold max'),
        ),
        migrations.AddField(
            model_name='imageanalysisparameter',
            name='sat_min',
            field=models.FloatField(default=0.0, verbose_name='Saturation threshold min'),
        ),
        migrations.AddField(
            model_name='imageanalysisparameter',
            name='val_max',
            field=models.FloatField(default=1.0, verbose_name='Value threshold max'),
        ),
        migrations.AddField(
            model_name='imageanalysisparameter',
            name='val_min',
            field=models.FloatField(default=0.0, verbose_name='Value threshold min'),
        ),
        migrations.AlterField(
            model_name='capturesession',
            name='period',
            field=models.CharField(choices=[('dt', 'Day time image'), ('nt', 'Night time image')], max_length=2, verbose_name='Day period'),
        ),
    ]
