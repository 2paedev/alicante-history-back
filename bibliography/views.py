from rest_framework import viewsets

from .models import Bibliography
from .serializers import BibliographySerializer


class BibliographyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bibliography.objects.all()
    serializer_class = BibliographySerializer
