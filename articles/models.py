import datetime

from django.db import models

from authors.models import Author
from custom_image.models import CustomImage
from tags.models import Tag


class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.ForeignKey(Author, related_name='article_author', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    date = models.DateField(default=datetime.date.today)
    images = models.ManyToManyField(CustomImage)
    text = models.CharField(max_length=10000, blank=False, null=False, default='')
    likes = models.PositiveIntegerField(blank=False, null=False, default=0)
    bibliography = models.CharField(max_length=10000, blank=False, null=False, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
