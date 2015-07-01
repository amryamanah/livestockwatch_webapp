# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0004_auto_20150629_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageanalysisresult',
            name='pupil_max_area',
        ),
    ]
