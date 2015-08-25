# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_article', '0011_auto_20150702_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='blockarticle',
            name='subtitle',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
