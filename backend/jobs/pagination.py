from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response

class JobListPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'pagecounts': self.page.paginator.num_pages,
            'current': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })