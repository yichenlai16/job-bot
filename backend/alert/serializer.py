from rest_framework import serializers
from .models import Alerts
from user_info.serializers import UserSerializer


class AlertSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Alerts
        fields = "__all__"
        depth = 0
