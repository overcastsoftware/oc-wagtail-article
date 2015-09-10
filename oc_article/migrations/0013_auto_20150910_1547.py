# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_article', '0012_auto_20150825_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='styles_override',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='blockarticle',
            name='styles_override',
            field=models.TextField(null=True, blank=True),
        ),
    ]
