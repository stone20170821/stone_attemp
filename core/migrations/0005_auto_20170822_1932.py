# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170822_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horsebasictemp',
            old_name='reversedPerShare',
            new_name='reservedPerShare',
        ),
    ]
