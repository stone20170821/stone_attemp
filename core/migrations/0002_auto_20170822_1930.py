# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horsebasictemp',
            old_name='fix_assets',
            new_name='fixAssets',
        ),
        migrations.RenameField(
            model_name='horsebasictemp',
            old_name='liquid_assets',
            new_name='liquidAssets',
        ),
        migrations.RenameField(
            model_name='horsebasictemp',
            old_name='reversed_per_share',
            new_name='reversedPerShare',
        ),
        migrations.RenameField(
            model_name='horsebasictemp',
            old_name='total_assets',
            new_name='totalAssets',
        ),
    ]
