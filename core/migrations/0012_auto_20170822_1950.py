# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170822_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horsebasictemp',
            name='bvps',
            field=models.DecimalField(verbose_name='\u6bcf\u80a1', max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='horsebasictemp',
            name='outstanding',
            field=models.DecimalField(verbose_name='\u6d41\u901a\u80a1\u672c\uff08\u4ebf\uff09', max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='horsebasictemp',
            name='pb',
            field=models.DecimalField(verbose_name='\u5e02\u51c0\u7387', max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='horsebasictemp',
            name='pe',
            field=models.DecimalField(verbose_name='\u5e02\u76c8\u7387', max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='horsebasictemp',
            name='profit',
            field=models.DecimalField(verbose_name='\u5229\u6da6\u540c\u6bd4\uff08%\uff09', max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='horsebasictemp',
            name='reservedPerShare',
            field=models.DecimalField(verbose_name='\u6bcf\u80a1\u516c\u79ef\u91d1', max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='horsebasictemp',
            name='rev',
            field=models.DecimalField(verbose_name='\u6536\u5165\u540c\u6bd4\uff08%\uff09', max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='horsebasictemp',
            name='totals',
            field=models.DecimalField(verbose_name='\u603b\u80a1\u672c\uff08\u4ebf\uff09', max_digits=14, decimal_places=4),
        ),
    ]
