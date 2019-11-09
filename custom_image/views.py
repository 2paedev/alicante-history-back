from rest_framework import viewsets

from .models import CustomImage
from .serializers import CustomImageSerializer


class CustomImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomImage.objects.all()
    serializer_class = CustomImageSerializer
