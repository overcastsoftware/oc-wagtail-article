# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('oc_article', '0005_article_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='oc_article.TaggedArticle', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='blockarticle',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='oc_article.TaggedArticle', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
