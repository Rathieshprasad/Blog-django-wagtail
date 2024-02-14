from django.db import models
import math
from wagtail.models import Page
from wagtail.fields import RichTextField,StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import ChoiceBlock
from wagtail.search import index

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+',blank=True,null=True)
    
    caption = models.CharField(blank=True, max_length=250)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('image'),
        FieldPanel('caption'),
        FieldPanel('category'),
    ]    

    category = StreamField([
        ('category', ChoiceBlock(choices=[
            ('HappyFox Help Desk', 'HappyFox Help Desk'),
            ('HappyFox Service Desk', 'HappyFox Service Desk'),
            ('HappyFox BI', 'HappyFox BI'),
            ('HappyFox ChatBot', 'HappyFox ChatBot'),
            ('Miscellaneous', 'Miscellaneous'),
        ])),
    ], blank=True)
    def get_related_posts(self):
        category = self.category 
        parent_page = self.get_parent().specific
        related_posts = parent_page.get_children().type(BlogPage).filter(category=category).exclude(id=self.id)[:3]
        return related_posts
    def get_reading_time(self):
        words_per_minute = 200
        total_words = len(self.body.split())
        reading_time_minutes = total_words / words_per_minute
        reading_time_minutes = math.ceil(reading_time_minutes)  
        return reading_time_minutes
    
    