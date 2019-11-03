from rest_framework import viewsets

from .models import Author
from .serializers import AuthorSerializer


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
