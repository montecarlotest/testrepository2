# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150810_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='area',
            field=models.IntegerField(default=0),
        ),
    ]
