from rest_framework import viewsets
from info.models import UserInfo
from .serializers import InfoSerializer


class InfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = InfoSerializer


