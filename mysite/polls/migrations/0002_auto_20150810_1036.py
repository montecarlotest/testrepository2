# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elecfee',
            old_name='department',
            new_name='bill',
        ),
        migrations.RenameField(
            model_name='gasfee',
            old_name='department',
            new_name='bill',
        ),
        migrations.RenameField(
            model_name='propertymanagefee',
            old_name='department',
            new_name='bill',
        ),
        migrations.RenameField(
            model_name='waterfee',
            old_name='department',
            new_name='bill',
        ),
        migrations.AddField(
            model_name='propertymanagefee',
            name='houseService',
            field=models.IntegerField(default=0),
        ),
    ]
