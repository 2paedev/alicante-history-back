from rest_framework import viewsets

from .models import Article
from .serializers import ArticleSerializer


class ArticlesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
