from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from alicante_history.shared.pagination import CustomResultsSetPagination

from .models import Article
from .serializers import ArticleSerializer


class ArticlesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomResultsSetPagination

    @action(detail=True, methods=['put'], name='Likes in articles')
    def like(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        data = {'likes': article.likes + 1}
        serializer = ArticleSerializer(article, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
