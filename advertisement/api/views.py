from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from advertisement.models import Advertisement
from advertisement.api.serializer import AdvertisementSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    permission_classes = [IsAuthenticated]
