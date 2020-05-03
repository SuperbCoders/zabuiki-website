from rest_framework import serializers

from zabuiki.account.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'social']

