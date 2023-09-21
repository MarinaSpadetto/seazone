from rest_framework import viewsets, status
from advertisement.models import Advertisement
from advertisement.api.serializer import AdvertisementSerializer
from rest_framework.response import Response


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
