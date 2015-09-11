from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from django.utils.translation import ugettext_lazy as _


class ImageBlock(blocks.StructBlock):
    images = blocks.ListBlock(blocks.StructBlock([
                ('image', ImageChooserBlock(formats=['full-width', 'left', 'right'], required=True)),
                ('caption', blocks.CharBlock(required=False)),
                ('image_type', blocks.ChoiceBlock(choices=(('header_image', 'Header image'), ('content_image', 'Content image'), ('full_width_content_image', 'Full width content image')), required=True)),
        ]))
    block_classes = blocks.CharBlock(required=False)

    class Meta:
        icon = 'image'


class BlockquoteBlock(blocks.StructBlock):
    blockquote = blocks.CharBlock(classname="full blockquote")
    block_classes = blocks.CharBlock(required=False)

    class Meta:
        icon = 'openquote'


class ParagraphBlock(blocks.StructBlock):
    paragraph = blocks.RichTextBlock()
    block_classes = blocks.CharBlock(required=False)

    class Meta:
        icon = 'bold'


class TableBlock(blocks.StructBlock):
    table = blocks.TextBlock(rows=10, help_text=_(u'Enter your table as comma separated values, one line for each row.'))
    caption = blocks.CharBlock()
    header_row = blocks.BooleanBlock(required=False, help_text=_(u'Render first row as header if checked'))
    header_column = blocks.BooleanBlock(required=False, help_text=_(u'Render first column as header if checked'))
    block_classes = blocks.CharBlock(required=False)


class CommonEditingBlock(blocks.StreamBlock):
    image_block = ImageBlock()
    paragraph_block = ParagraphBlock()
    blockquote_block = BlockquoteBlock()
    html = blocks.RawHTMLBlock()
    embed = EmbedBlock(icon='media')
    table_block = TableBlock()