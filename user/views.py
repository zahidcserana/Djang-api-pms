from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, request, status, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404


# {"code":20000,"data":{"status":"success"}}


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['id', 'name', 'email', 'mobile', 'status', 'type']
    ordering_fields = ['id', 'name']

    # ordering = ('-id')

    def create(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)

    def update(self, request, pk=None):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data
        serializer = UserSerializer(
            instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)


# class UserUpdate(APIView):
#     def put(self, request):
#         content = {"code": 20000, "data": {"status": "success"}}
#         return Response(content)


class UserView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email', 'mobile']


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

# class UserInfo(APIView):

#     def get(self, request):
#         content = {"code":20000,"data":{"roles":["admin"],"introduction":"I am a super administrator","avatar":"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif","name":"Super Admin"}}
#         return Response(content)
