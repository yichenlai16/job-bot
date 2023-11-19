from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import viewsets, generics
from rest_framework.views import APIView

from .models import Alerts
from .serializer import AlertSerializer
from django.contrib.auth.models import User

# Create your views here.


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alerts.objects.all()
    serializer_class = AlertSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def create(self, request):
    #     print("this is a post request", request.user, request.data)
    #     return Response(request)


class UserAlertViewSet(generics.ListAPIView):
    serializer_class = AlertSerializer

    def get_queryset(self):
        # users = User.objects.get(username=self.request.user)

        # # users = self.request.user
        # print("***")
        # print(users)
        # print(type(users))
        # print("***")
        # return Alerts.objects.filter(user=users)
        return Alerts.objects.filter(user=self.request.user)
