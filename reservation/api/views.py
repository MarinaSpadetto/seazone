from rest_framework import viewsets
from reservation.models import Reservation
from reservation.api.serializer import ReservationSerializers


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers
    http_method_names = ['get', 'post', 'delete']
