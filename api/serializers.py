from rest_framework import serializers
from info.models import UserInfo


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('name', 'address', 'email')
