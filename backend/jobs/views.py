from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Jobs, Companys

from .serializers import JobSerializer, CompanyDetailSerializer

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .pagination import JobListPagination
from .filter import JobFilter
from django.contrib.auth.models import User
from user_info.models import User_Info
from alert.models import Alerts
from datetime import date
import json

# Create your views here.


class JobViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    pagination_class = JobListPagination
    filter_backends = [DjangoFilterBackend]

    filter_class = JobFilter

    def perform_create(self, serializer):
        serializer.save(
            # company=self.request.company,
            category=self.request.category
        )


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Companys.objects.all()
    serializer_class = CompanyDetailSerializer
    pagination_class = JobListPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class MainView(APIView):
    def get(self, request):
        users = User.objects.get(username=request.user)
        notifyTotal = Alerts.objects.filter(user_id=users).count()
        jobTotal = Jobs.objects.count()
        todayTotal = Jobs.objects.filter(import_date=date.today()).count()
        data = {
            "notifyTotal": notifyTotal,
            "jobTotal": jobTotal,
            "todayTotal": todayTotal,
        }
        return HttpResponse(json.dumps(data), content_type="application/json")


# Create your views here.
