from django.urls import path, include
from rest_framework import routers
from advertisement.api.views import AdvertisementViewSet

router = routers.DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet,
                basename='Advertisements')


urlpatterns = [
    path('', include(router.urls)),
]
