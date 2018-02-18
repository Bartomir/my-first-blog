# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180218_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('model_pic', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_file',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
