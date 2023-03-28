from rest_framework import serializers
from .models import Udata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Udata
        fields = ['id', 'uname', 'email']