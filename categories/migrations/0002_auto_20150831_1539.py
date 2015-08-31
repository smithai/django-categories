# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import base.staticstorages


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='thumbnail',
            field=models.FileField(storage=base.staticstorages.S3BotoStorage(), null=True, upload_to=b'uploads/categories/thumbnails', blank=True),
        ),
    ]
