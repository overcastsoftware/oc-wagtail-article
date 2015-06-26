# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(null=True, blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='BlockArticle',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(null=True, blank=True)),
                ('body', wagtail.wagtailcore.fields.StreamField([(b'image_block', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True, formats=[b'full-width', b'left', b'right'])), (b'caption', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'image_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'header_image', b'Header image'), (b'content_image', b'Content image')]))], icon=b''))), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'blockquote', wagtail.wagtailcore.blocks.CharBlock(classname=b'full blockquote')), (b'fullimage', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'video_block', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'video', wagtail.wagtailembeds.blocks.EmbedBlock(required=True)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True, formats=[b'full-width', b'left', b'right']))], icon=b''))), (b'html', wagtail.wagtailcore.blocks.RawHTMLBlock(classname=b'full title'))])),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
