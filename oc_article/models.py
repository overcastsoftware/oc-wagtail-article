from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from oc_core.panels import ColorFieldPanel

from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager


class ArticleTag(TaggedItemBase):
    content_object = ParentalKey('Article', null=True, blank=True, related_name="%(app_label)s_%(class)s_taggeditems")


class BlockArticleTag(TaggedItemBase):
    content_object = ParentalKey('BlockArticle', null=True, blank=True, related_name="%(app_label)s_%(class)s_taggeditems")


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name=_('Title'))
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255)

    panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('slug', classname="col6"),
        ColorFieldPanel('color', classname="col6 colorpicker-field"),
    ]

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
        return u"%s" % self.title

register_snippet(Category)


class ArticleMixin(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField(null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    excerpt = RichTextField(blank=True, verbose_name=_('Excerpt'))

    class Meta:
        abstract = True

BASE_ARTICLE_CONTENT_PANELS = [
    FieldPanel('title'),
    MultiFieldPanel([
        FieldPanel('author', classname="col6"),
        FieldPanel('date', classname="col6"),
    ], "Author and date"),
    SnippetChooserPanel('category', Category),
    FieldPanel('excerpt'),
]


class Article(Page, ArticleMixin):
    """
    Basic article with a rich text editor for body.
    """
    tags = ClusterTaggableManager(through=ArticleTag, blank=True)
    body = RichTextField(blank=True)
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


Article.content_panels = BASE_ARTICLE_CONTENT_PANELS + [
    FieldPanel('tags'),
    ImageChooserPanel('header_image'),
    FieldPanel('body'),
]


class BlockArticle(Page, ArticleMixin):
    """
    Article built with multiple types of blocks.
    Blocks can be repeated and/or combined in any way.
    """
    tags = ClusterTaggableManager(through=BlockArticleTag, blank=True)
    body = StreamField([
        ('image_block', blocks.ListBlock(blocks.StructBlock([
            ('image', ImageChooserBlock(formats=['full-width', 'left', 'right'], required=True)),
            ('caption', blocks.CharBlock(required=True)),
            ('image_type', blocks.ChoiceBlock(choices=(('header_image', 'Header image'), ('content_image', 'Content image')), required=True)),
        ], icon=''))),
        ('paragraph', blocks.RichTextBlock()),
        ('blockquote', blocks.CharBlock(classname="full blockquote")),
        ('fullimage', ImageChooserBlock()),
        ('video_block', blocks.ListBlock(blocks.StructBlock([
            ('video', EmbedBlock(required=True)),
            ('image', ImageChooserBlock(formats=['full-width', 'left', 'right'], required=True)),
        ], icon=''))),
        ('html', blocks.RawHTMLBlock(classname="full title")),
    ])


BlockArticle.content_panels = BASE_ARTICLE_CONTENT_PANELS + [
    FieldPanel('tags'),
    StreamFieldPanel('body'),
]
