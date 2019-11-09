from rest_framework import serializers

from articles.models import Article
from articles.serializers import ArticleSerializer

from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField('get_articles_by_tags')

    def get_articles_by_tags(self, resume):
        all_tags = resume.tags.all()
        result = []
        for tag in all_tags:
            qs = Article.objects.filter(tags=tag.id)
            for article in qs:
                serializer = ArticleSerializer(instance=article)
                result.append(serializer.data)
        return result

    class Meta:
        model = Resume
        fields = '__all__'
        depth = 1


class ResumeSerializerLastFive(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField('get_articles_by_tags')

    def get_articles_by_tags(self, resume):
        last_five = Article.objects.all().order_by('created')[:5][::-1]
        result = []
        for article in last_five:
            serializer = ArticleSerializer(instance=article)
            result.append(serializer.data)
        return result

    class Meta:
        model = Resume
        fields = '__all__'
        depth = 1
