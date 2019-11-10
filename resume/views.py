from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from articles.models import Article
from articles.serializers import ArticleSerializer

from .models import Resume
from .serializers import ResumeSerializer


class ResumeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    @action(detail=False, methods=['GET'], name='Get last five articles')
    def lastfive(self, request, *args, **kwargs):
        last_five_articles = Article.objects.all().order_by('created')[:5][::-1]
        serializer_last_five = ArticleSerializer(last_five_articles, many=True)
        return Response(serializer_last_five.data)
