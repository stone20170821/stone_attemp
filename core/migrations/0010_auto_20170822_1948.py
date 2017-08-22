# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170822_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horsebasictemp',
            name='esp',
            field=models.DecimalField(verbose_name='\u6bcf\u80a1\u6536\u76ca', max_digits=7, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='horsebasictemp',
            name='gpr',
            field=models.DecimalField(verbose_name='\u6bdb\u5229\u7387\uff08%\uff09', max_digits=7, decimal_places=4),
        ),
    ]
