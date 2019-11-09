from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    title = 'Últimos 5 artículos'
    image = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = '__all__'

    def get_image(self, author):
        return author.image.url
