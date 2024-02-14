from django.db import models
import math
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
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
    ]    

    def get_reading_time(self):
        words_per_minute = 200
        total_words = len(self.body.split())
        reading_time_minutes = total_words / words_per_minute
        reading_time_minutes = math.ceil(reading_time_minutes)  
        return reading_time_minutes