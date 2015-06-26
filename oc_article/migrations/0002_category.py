# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title', db_index=True)),
                ('slug', models.SlugField(max_length=255, null=True, verbose_name='Slug', blank=True)),
                ('color', models.CharField(max_length=255)),
            ],
        ),
    ]
