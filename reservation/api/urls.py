from django.urls import path, include
from rest_framework import routers
from reservation.api.views import ReservationViewSet

router = routers.DefaultRouter()
router.register(r'reservations', ReservationViewSet, basename='Reservations')


urlpatterns = [
    path('', include(router.urls)),
]
