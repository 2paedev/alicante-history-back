from rest_framework import viewsets

from .models import EmailSubscription
from .serializers import EmailSubscriptionSerializer


class EmailSubscriptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer
