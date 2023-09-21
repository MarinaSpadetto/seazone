from django.urls import path, include
from rest_framework import routers
from property.api.views import PropertyViewSet

router = routers.DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='Properties')


urlpatterns = [
    path('', include(router.urls)),
]
