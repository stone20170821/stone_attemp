# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20170828_1840'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='horsebasicbackup',
            table='horse_basic_backup',
        ),
    ]
