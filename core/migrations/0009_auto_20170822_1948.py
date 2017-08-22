# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170822_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horsebasictemp',
            name='perundp',
            field=models.DecimalField(verbose_name='\u6bcf\u80a1\u672a\u5206', max_digits=7, decimal_places=4),
        ),
    ]
