# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('oc_article', '0007_auto_20150701_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockArticleTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='articletag',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='articletag',
            name='object_id',
        ),
        migrations.AddField(
            model_name='articletag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(related_name='oc_article_articletag_taggeditems', blank=True, to='oc_article.Article', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='oc_article.ArticleTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='blockarticle',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='oc_article.BlockArticleTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='blockarticletag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(related_name='oc_article_blockarticletag_taggeditems', blank=True, to='oc_article.Article', null=True),
        ),
        migrations.AddField(
            model_name='blockarticletag',
            name='tag',
            field=models.ForeignKey(related_name='oc_article_blockarticletag_items', to='taggit.Tag'),
        ),
    ]
