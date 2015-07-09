# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodData1',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('va', models.FloatField(verbose_name='Vitamin A (IU/dl)', null=True)),
                ('beta_carotene', models.FloatField(verbose_name='Beta carotene (ug/dl)', null=True)),
                ('ve', models.FloatField(verbose_name='Vitamin E (ug/dl)', null=True)),
                ('date_taken', models.DateField(verbose_name='Date taken', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BloodData2',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('vc', models.FloatField(verbose_name='Vitamin C (IU/dl)', null=True)),
                ('date_taken', models.DateField(verbose_name='Date taken', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BodyData1',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('weight', models.FloatField(verbose_name='Weight (kg)', null=True)),
                ('withers_height', models.FloatField(verbose_name='Withers height (cm)', null=True)),
                ('chest_circumference', models.FloatField(verbose_name='Chest circumference (cm)', null=True)),
                ('date_taken', models.DateField(verbose_name='Date taken', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BodyData2',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('hip_height', models.FloatField(verbose_name='Hip height (cm)', null=True)),
                ('body_length', models.FloatField(verbose_name='Body length (cm)', null=True)),
                ('chest_depth', models.FloatField(verbose_name='Chest weight (cm)', null=True)),
                ('chest_width', models.FloatField(verbose_name='Chest width (cm)', null=True)),
                ('buttocks_length', models.FloatField(verbose_name='Buttocks length (cm)', null=True)),
                ('hip_width', models.FloatField(verbose_name='Hip width (cm)', null=True)),
                ('thurl_width', models.FloatField(verbose_name='Thurl width (cm)', null=True)),
                ('pin_bone_width', models.FloatField(verbose_name='Pin bone width (cm)', null=True)),
                ('date_taken', models.DateField(verbose_name='Date taken', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BodyTemp',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('temp', models.FloatField(verbose_name='Temp (C)', null=True)),
                ('time_taken', models.DateTimeField(verbose_name='Time taken', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cattle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('id_number', models.CharField(verbose_name='id_number', unique=True, max_length=12)),
                ('regist_num_father', models.CharField(max_length=12, verbose_name='regist_num_father')),
                ('regist_num_mother', models.CharField(max_length=12, verbose_name='regist_num_mother')),
                ('sex', models.CharField(max_length=2, default='F', verbose_name='sex', choices=[('M', 'Male'), ('F', 'Female'), ('CM', 'Castrated Male')])),
                ('birthday', models.DateField(verbose_name='birthday', null=True, blank=True)),
                ('fat_start_date', models.DateField(verbose_name='fat_start_date', null=True, blank=True)),
                ('fat_finish_date', models.DateField(verbose_name='fat_finish_date', null=True, blank=True)),
                ('examination_number', models.CharField(max_length=10, verbose_name='Examination number')),
            ],
        ),
        migrations.CreateModel(
            name='CattleNeckband',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
                ('start_date', models.DateField(verbose_name='start_date', null=True, blank=True)),
                ('end_date', models.DateField(verbose_name='end_date', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoarseFeedComponent',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('identifier', models.CharField(verbose_name='Coarse feed identifier', unique=True, max_length=30)),
                ('crude_protein_mv', models.FloatField(verbose_name='Crude protein', null=True)),
                ('crude_protein_dc', models.FloatField(verbose_name='Crude protein digestion coefficient', null=True)),
                ('crude_fat_mv', models.FloatField(verbose_name='Crude fat', null=True)),
                ('crude_fat_dc', models.FloatField(verbose_name='Crude fat digestion coefficient', null=True)),
                ('nitrogen_free_extract_mv', models.FloatField(verbose_name='Nitrogen free extract', null=True)),
                ('nitrogen_free_extract_dc', models.FloatField(verbose_name='Nitrogen free extract digestion coefficient', null=True)),
                ('crude_fiber_mv', models.FloatField(verbose_name='Crude fiber', null=True)),
                ('crude_fiber_dc', models.FloatField(verbose_name='Crude fiber digestion coefficient', null=True)),
                ('total_digestible_nutrient', models.FloatField(verbose_name='Total digestible nutrient', null=True)),
                ('beta_carotene_content', models.FloatField(verbose_name='Beta carotene content', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeedData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('coarse_feed_dosage', models.FloatField(verbose_name='Coarse feed dosage', null=True)),
                ('coarse_feed_residue', models.FloatField(verbose_name='Coarse feed residue', null=True)),
                ('concentrate_feed_dosage', models.FloatField(verbose_name='Concentrate feed dosage', null=True)),
                ('concentrate_feed_residue', models.FloatField(verbose_name='Concentrate feed residue', null=True)),
                ('vit_prep_concentrate_feed', models.FloatField(verbose_name='Concentrate feed vitamin preparation', null=True)),
                ('vit_prep_kyoto', models.FloatField(verbose_name='Vitamin preparation direct administration Kyoto', null=True)),
                ('vit_prep_hyogo', models.FloatField(verbose_name='Vitamin preparation direct administration Hyogo', null=True)),
                ('date_taken', models.DateField(verbose_name='Date taken', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NeckbandPattern',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('pattern', models.CharField(verbose_name='pattern', unique=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RemarksData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('remarks', models.TextField(verbose_name='Remarks')),
                ('date_taken', models.DateField(verbose_name='Date taken', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QualityYieldData',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified', auto_now=True)),
                ('cattle', models.OneToOneField(serialize=False, primary_key=True, to='cattle_app.Cattle')),
                ('rib_eye_area', models.FloatField(verbose_name='Rib eye area', null=True)),
                ('beef_flank_thickness', models.FloatField(verbose_name='Beef flank thickness', null=True)),
                ('subcutaneous_fat_thickness', models.FloatField(verbose_name='Subcutaneous (under the skin) fat', null=True)),
                ('yield_ratio_std_val', models.FloatField(verbose_name='Yield ratio standard value', null=True)),
                ('bms', models.FloatField(verbose_name='Beef marbling standard', null=True)),
                ('carcass_weight', models.FloatField(verbose_name='Carcass weight', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='remarksdata',
            name='cattle',
            field=models.ForeignKey(to='cattle_app.Cattle'),
        ),
        migrations.AddField(
            model_name='feeddata',
            name='cattle',
            field=models.ForeignKey(to='cattle_app.Cattle'),
        ),
        migrations.AddField(
            model_name='feeddata',
            name='coarse_feed_component',
            field=models.ForeignKey(to='cattle_app.CoarseFeedComponent'),
        ),
        migrations.AddField(
            model_name='cattleneckband',
            name='cattle',
            field=models.ForeignKey(to='cattle_app.Cattle'),
        ),
        migrations.AddField(
            model_name='cattleneckband',
            name='neckband_pattern',
            field=models.ForeignKey(to='cattle_app.NeckbandPattern'),
        ),
        migrations.AddField(
            model_name='cattle',
            name='stall',
            field=models.ForeignKey(to='farm_app.Stall'),
        ),
        migrations.AddField(
            model_name='bodytemp',
            name='cattle',
            field=models.ForeignKey(to='cattle_app.Cattle'),
        ),
        migrations.AddField(
            model_name='bodydata2',
            name='cattle',
            field=models.ForeignKey(to='cattle_app.Cattle'),
        ),
        migrations.AddField(
            model_name='bodydata1',
            name='cattle',
            field=models.ForeignKey(to='cattle_app.Cattle'),
        ),
        migrations.AddField(
            model_name='blooddata2',
            name='cattle',
            field=models.ForeignKey(to='cattle_app.Cattle'),
        ),
        migrations.AddField(
            model_name='blooddata1',
            name='cattle',
            field=models.ForeignKey(to='cattle_app.Cattle'),
        ),
        migrations.AlterUniqueTogether(
            name='remarksdata',
            unique_together=set([('cattle', 'date_taken')]),
        ),
        migrations.AlterUniqueTogether(
            name='feeddata',
            unique_together=set([('cattle', 'date_taken')]),
        ),
        migrations.AlterUniqueTogether(
            name='cattle',
            unique_together=set([('id_number', 'examination_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='bodytemp',
            unique_together=set([('cattle', 'time_taken')]),
        ),
        migrations.AlterUniqueTogether(
            name='bodydata2',
            unique_together=set([('cattle', 'date_taken')]),
        ),
        migrations.AlterUniqueTogether(
            name='bodydata1',
            unique_together=set([('cattle', 'date_taken')]),
        ),
        migrations.AlterUniqueTogether(
            name='blooddata2',
            unique_together=set([('cattle', 'date_taken')]),
        ),
        migrations.AlterUniqueTogether(
            name='blooddata1',
            unique_together=set([('cattle', 'date_taken')]),
        ),
    ]
