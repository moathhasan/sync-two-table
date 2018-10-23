from .models import LocalVlans, RemoteVlans
from rest_framework import viewsets
from .Serializers import  UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LocalVlans.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = RemoteVlans.objects.all()
    serializer_class = GroupSerializer