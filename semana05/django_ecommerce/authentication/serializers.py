from rest_framework import serializers
from authentication.models import RoleModel, UserModel


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'