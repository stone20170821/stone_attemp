# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170822_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horsebasictemp',
            name='esp',
            field=models.DecimalField(verbose_name='\u6bcf\u80a1\u6536\u76ca', max_digits=9, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='horsebasictemp',
            name='gpr',
            field=models.DecimalField(verbose_name='\u6bdb\u5229\u7387\uff08%\uff09', max_digits=9, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='horsebasictemp',
            name='npr',
            field=models.DecimalField(verbose_name='\u51c0\u5229\u6da6\u7387\uff08%\uff09', max_digits=9, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='horsebasictemp',
            name='perundp',
            field=models.DecimalField(verbose_name='\u6bcf\u80a1\u672a\u5206', max_digits=9, decimal_places=4),
        ),
    ]
