# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('oc_article', '0009_auto_20150702_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockarticle',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'image_block', wagtail.wagtailcore.blocks.StructBlock([(b'images', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True, formats=[b'full-width', b'left', b'right'])), (b'caption', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'image_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'header_image', b'Header image'), (b'content_image', b'Content image')]))]))), (b'block_classes', wagtail.wagtailcore.blocks.CharBlock())])), (b'paragraph_block', wagtail.wagtailcore.blocks.StructBlock([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'block_classes', wagtail.wagtailcore.blocks.CharBlock())])), (b'blockquote_block', wagtail.wagtailcore.blocks.StructBlock([(b'blockquote', wagtail.wagtailcore.blocks.CharBlock(classname=b'full blockquote')), (b'block_classes', wagtail.wagtailcore.blocks.CharBlock())])), (b'html', wagtail.wagtailcore.blocks.RawHTMLBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())]),
        ),
    ]
