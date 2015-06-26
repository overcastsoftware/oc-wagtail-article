# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('oc_article', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.IntegerField(verbose_name='Object id', db_index=True)),
                ('content_type', models.ForeignKey(related_name='oc_article_taggedarticle_tagged_items', verbose_name='Content type', to='contenttypes.ContentType')),
                ('tag', models.ForeignKey(related_name='oc_article_taggedarticle_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='oc_article.Category', null=True),
        ),
        migrations.AddField(
            model_name='blockarticle',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='oc_article.Category', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='oc_article.TaggedArticle', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='blockarticle',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='oc_article.TaggedArticle', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
