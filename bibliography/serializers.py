from rest_framework import serializers

from .models import Bibliography


class BibliographySerializer(serializers.ModelSerializer):

    class Meta:
        model = Bibliography
        fields = '__all__'
