# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oc_article', '0003_auto_20150626_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='Excerpt', blank=True),
        ),
        migrations.AddField(
            model_name='blockarticle',
            name='excerpt',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='Excerpt', blank=True),
        ),
    ]
