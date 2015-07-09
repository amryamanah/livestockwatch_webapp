# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisCaptureSessionResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('pupil_max_area', models.FloatField(verbose_name='IAR pupil max area', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CaptureSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='CS Name', null=True)),
                ('period', models.CharField(max_length=2, verbose_name='Day period', choices=[('dt', 'Day time image'), ('nt', 'Night time image')])),
                ('folder_path', models.CharField(max_length=300, verbose_name='CS folder path', null=True)),
                ('time_taken', models.DateTimeField(verbose_name='CS time taken', null=True)),
                ('cattle', models.ForeignKey(to='cattle_app.Cattle')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnalysisParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('hue_max', models.FloatField(default=1.0, verbose_name='Hue threshold max')),
                ('hue_min', models.FloatField(default=0.0, verbose_name='Hue threshold min')),
                ('sat_max', models.FloatField(default=1.0, verbose_name='Saturation threshold max')),
                ('sat_min', models.FloatField(default=0.0, verbose_name='Saturation threshold min')),
                ('val_max', models.FloatField(default=1.0, verbose_name='Value threshold max')),
                ('val_min', models.FloatField(default=0.0, verbose_name='Value threshold min')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnalysisResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('img_result_path', models.FilePathField(max_length=300, verbose_name='Image analysis result path', recursive=True, null=True)),
                ('result_type', models.IntegerField(verbose_name='IAR analysis state', choices=[(0, 'No pupil detected'), (1, 'Impartial pupil detected'), (2, 'Pupil detected')], null=True)),
                ('pl_distance', models.FloatField(verbose_name='IAR pl distance', null=True)),
                ('nopl_distance', models.FloatField(verbose_name='IAR nopl distance', null=True)),
                ('pupil_avg_red', models.FloatField(verbose_name='IAR pupil red channel average', null=True)),
                ('pupil_avg_green', models.FloatField(verbose_name='IAR pupil green channel average', null=True)),
                ('pupil_avg_blue', models.FloatField(verbose_name='IAR pupil blue channel average', null=True)),
                ('pupil_eccentricity', models.FloatField(verbose_name='IAR pupil eccentricity', null=True)),
                ('pupil_area', models.FloatField(verbose_name='IAR pupil area', null=True)),
                ('pupil_ca', models.FloatField(verbose_name='IAR constriction amplitude', null=True)),
                ('pupil_perimeter', models.FloatField(verbose_name='IAR pupil perimeter', null=True)),
                ('pupil_major_axis_length', models.FloatField(verbose_name='IAR pupil major axis length', null=True)),
                ('pupil_minor_axis_length', models.FloatField(verbose_name='IAR pupil minor axis length', null=True)),
                ('pupil_ipr', models.FloatField(verbose_name='IAR initial pupil roundness', null=True)),
                ('pupil_normalized_area', models.FloatField(verbose_name='IAR pupil normalized area', null=True)),
                ('time_taken', models.DateTimeField(verbose_name='IAR time taken', null=True)),
                ('analysis_parameter', models.ForeignKey(to='image_app.ImageAnalysisParameter')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnalysisSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('name', models.CharField(max_length=300, verbose_name='IAS name')),
                ('remarks', models.TextField(verbose_name='IAS remarks', blank=True, null=True)),
                ('analysis_state', models.IntegerField(default=0, verbose_name='IAS analysis state', choices=[(2, 'Finish'), (1, 'In Progress'), (0, 'Pending')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RawImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('name', models.CharField(max_length=300, verbose_name='RI name')),
                ('image_type', models.CharField(max_length=4, verbose_name='RI image type', choices=[('PL', 'Polarized Filter'), ('NOPL', 'Non Polarized Filter'), ('ID', 'Identification')])),
                ('time_taken', models.DateTimeField(verbose_name='RI time taken', null=True)),
                ('image_file', models.FileField(verbose_name='RI image file', upload_to=image_app.models.generate_filepath)),
                ('capture_session', models.ForeignKey(to='image_app.CaptureSession')),
            ],
        ),
        migrations.AddField(
            model_name='imageanalysisresult',
            name='analysis_session',
            field=models.ForeignKey(to='image_app.ImageAnalysisSession'),
        ),
        migrations.AddField(
            model_name='imageanalysisresult',
            name='raw_image',
            field=models.ForeignKey(to='image_app.RawImage'),
        ),
        migrations.AddField(
            model_name='imageanalysisparameter',
            name='analysis_session',
            field=models.ForeignKey(to='image_app.ImageAnalysisSession'),
        ),
        migrations.AddField(
            model_name='imageanalysisparameter',
            name='capture_session',
            field=models.ForeignKey(to='image_app.CaptureSession'),
        ),
        migrations.AddField(
            model_name='analysiscapturesessionresult',
            name='analysis_parameter',
            field=models.ForeignKey(to='image_app.ImageAnalysisParameter'),
        ),
        migrations.AddField(
            model_name='analysiscapturesessionresult',
            name='analysis_session',
            field=models.ForeignKey(to='image_app.ImageAnalysisSession'),
        ),
        migrations.AlterUniqueTogether(
            name='rawimage',
            unique_together=set([('name', 'capture_session')]),
        ),
        migrations.AlterUniqueTogether(
            name='imageanalysisresult',
            unique_together=set([('analysis_session', 'raw_image')]),
        ),
        migrations.AlterUniqueTogether(
            name='imageanalysisparameter',
            unique_together=set([('analysis_session', 'capture_session')]),
        ),
        migrations.AlterUniqueTogether(
            name='capturesession',
            unique_together=set([('cattle', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='analysiscapturesessionresult',
            unique_together=set([('analysis_session', 'analysis_parameter')]),
        ),
    ]
