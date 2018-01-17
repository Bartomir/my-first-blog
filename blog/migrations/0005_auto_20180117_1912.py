# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180117_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='model_pic',
            new_name='image_file',
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
