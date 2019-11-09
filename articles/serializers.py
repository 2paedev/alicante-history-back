from rest_framework import serializers

from authors.serializers import AuthorSerializer
from custom_image.serializers import CustomImageSerializer

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    images = CustomImageSerializer(many=True)
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = '__all__'
        depth = 1
