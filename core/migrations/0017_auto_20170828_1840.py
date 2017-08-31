# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20170828_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horsebasic',
            name='area',
            field=models.CharField(default='\u672a\u77e5', max_length=50, null=True, verbose_name='\u5730\u533a'),
        ),
        migrations.AlterField(
            model_name='horsebasicbackup',
            name='area',
            field=models.CharField(default='\u672a\u77e5', max_length=50, null=True, verbose_name='\u5730\u533a'),
        ),
    ]
