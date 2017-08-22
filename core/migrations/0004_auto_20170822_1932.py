# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170822_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horsebasictemp',
            old_name='reversed',
            new_name='reserved',
        ),
    ]
