# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170822_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horsebasictemp',
            name='bvps',
            field=models.DecimalField(verbose_name='\u6bcf\u80a1\u51c0\u8d44', max_digits=14, decimal_places=4),
        ),
    ]
