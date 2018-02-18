# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180218_1802'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExampleModel',
        ),
    ]
