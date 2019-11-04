from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True,)

    class Meta:
        model = Article
        fields = '__all__'
        depth = 1
