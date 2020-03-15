from .models import Department
from .serializers import DepartmentSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']


class UserInfo(APIView):

    def get(self, request):
        content = {"code": 20000, "data": {"roles": ["admin"], "introduction": "I am a super administrator",
                                           "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
                                           "name": "Super Admin"}}
        return Response(content)
