# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170822_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horsebasictemp',
            name='npr',
            field=models.DecimalField(verbose_name='\u51c0\u5229\u6da6\u7387\uff08%\uff09', max_digits=10, decimal_places=4),
        ),
    ]
