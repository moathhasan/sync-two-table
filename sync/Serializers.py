from .models import LocalVlans , RemoteVlans
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalVlans
        fields = ('name', 'vlan_id', 'descriptionl')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RemoteVlans
        fields = ('name', 'vlan_id' , 'description')