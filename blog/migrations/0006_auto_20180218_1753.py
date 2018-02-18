# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180117_1912'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_file',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
