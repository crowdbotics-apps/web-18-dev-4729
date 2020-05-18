from rest_framework import authentication
from ytytyt.models import Fmnhkjmnbmb
from .serializers import FmnhkjmnbmbSerializer
from rest_framework import viewsets


class FmnhkjmnbmbViewSet(viewsets.ModelViewSet):
    serializer_class = FmnhkjmnbmbSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Fmnhkjmnbmb.objects.all()
