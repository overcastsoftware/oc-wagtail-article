# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oc_article', '0008_auto_20150701_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockarticletag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(related_name='oc_article_blockarticletag_taggeditems', blank=True, to='oc_article.BlockArticle', null=True),
        ),
    ]
