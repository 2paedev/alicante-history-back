from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    model = Article
