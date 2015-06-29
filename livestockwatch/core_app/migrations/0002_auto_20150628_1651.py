# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cattle',
            name='examination_number',
            field=models.CharField(max_length=10, verbose_name='Examination number', default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='cattle',
            unique_together=set([('id_number', 'examination_number')]),
        ),
    ]
