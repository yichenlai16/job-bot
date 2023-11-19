from django.conf import settings
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os


class IndexTemplateView(TemplateView):
    def get_template_names(self):
        template_name = "index.html"
        return template_name


class demo(APIView):
    def post(self, request, format=None):
        # process = CrawlerProcess()
        # process.crawl(a104_firstpage)
        # process.start()
        cmd = "cd scrapy_project && scrapy crawl 104test"
        os.system(cmd)
        return HttpResponse("done")
