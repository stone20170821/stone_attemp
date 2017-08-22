# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170822_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horsebasictemp',
            old_name='fixAssets',
            new_name='fixedAssets',
        ),
    ]
