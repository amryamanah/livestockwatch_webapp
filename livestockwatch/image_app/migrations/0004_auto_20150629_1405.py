# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0003_auto_20150629_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analysiscapturesessionresult',
            old_name='image_analysis_parameter',
            new_name='analysis_parameter',
        ),
        migrations.AlterUniqueTogether(
            name='analysiscapturesessionresult',
            unique_together=set([('analysis_session', 'analysis_parameter')]),
        ),
    ]
