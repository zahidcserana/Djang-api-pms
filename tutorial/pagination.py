from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    def get_paginated_response(self, data):
        return Response({
           'next': self.get_next_link(),
           'previous': self.get_previous_link(),
           'count': self.page.paginator.count,
           'page': self.page.number,
            'num_page': self.page.paginator.num_pages,
            'results': data
        })

