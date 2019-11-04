from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer


class ArticlesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=False)
    def resume(self, request):
        data = Article.objects.all()
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(data, many=True)
        return Response({'something': 'my custom JSON'})
