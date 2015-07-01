# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0002_auto_20150629_0325'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisCaptureSessionResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('pupil_max_area', models.FloatField(verbose_name='IAR pupil max area', null=True)),
                ('analysis_session', models.ForeignKey(to='image_app.ImageAnalysisSession')),
                ('image_analysis_parameter', models.ForeignKey(to='image_app.ImageAnalysisParameter')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='analysiscapturesessionresult',
            unique_together=set([('analysis_session', 'image_analysis_parameter')]),
        ),
    ]
