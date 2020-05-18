from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FmnhkjmnbmbViewSet

router = DefaultRouter()
router.register("fmnhkjmnbmb", FmnhkjmnbmbViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
