from django.db import models

from articles.models import Article
from tags.models import Tag


class Resume(models.Model):
    title = models.CharField(blank=False, default='', max_length=80)
    tags = models.ManyToManyField(Tag)
    articles = models.ManyToManyField(Article, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
