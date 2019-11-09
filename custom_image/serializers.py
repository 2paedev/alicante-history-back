from rest_framework import serializers

from .models import CustomImage


class CustomImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = CustomImage
        fields = '__all__'

    def get_url(self, custom_image):
        return custom_image.url.url
