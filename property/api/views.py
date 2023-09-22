from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from property.models import Property
from property.api.serializer import PropertySerializer
from django_filters.rest_framework import DjangoFilterBackend


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cod_property']
    permission_classes = [IsAuthenticated]
