from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
import json
from .models import User_Info
from rest_framework.relations import RelatedField

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password']

    def validate(self, attrs):
        username = attrs.get('username')
        self.user = User.objects.get(username=username)
        # Do the verification with the phone_code here, if error, return a response with an error status code

        refresh = self.get_token(self.user)
        data = {}
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'last_name',
            'first_name',
            'email',
            'last_login',
            'date_joined'
        ]

class UserRegisterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='username')

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'password',
            'is_superuser'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'is_superuser': {'read_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)


class AuthUserSerializer(serializers.ModelSerializer):
    line_id = serializers.CharField(source='username')
    lastlogin = serializers.DateTimeField(
        source='last_login',
        format='%Y/%m/%d %H:%M:%S',

    )

    class Meta:
        model = User
        fields = ['id', 'line_id', 'lastlogin']


class User_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = ['user', 'uid','name','pic_url','notify_token','notification' ]
        depth = 0

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='profile.id')
    name = serializers.CharField(source='profile.name')
    notify_token = serializers.CharField(source='profile.notify_token')
    class Meta:
        model = User
        fields = ['id','name','notify_token']

class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = ['user', 'uid', 'notify_token', 'notification']