# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AddField(
            model_name='token',
            name='uid',
            field=models.CharField(max_length=40, default=uuid.uuid4),
        ),
    ]
