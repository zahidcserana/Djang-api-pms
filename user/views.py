# from .models import User
from django.contrib.auth.models import User

from setting.models import Department
from .serializers import UserSerializer
from rest_framework import viewsets, request, status, filters, generics
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from django.http import HttpResponse


# {"code":20000,"data":{"status":"success"}}


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']
    # filterset_fields = ['id', 'name', 'email', 'mobile', 'status', 'type']
    ordering_fields = ['id', 'username']

    def get_queryset(self):
        queryset = User.objects.all()
        # status = self.request.query_params.get('status')
        #
        # if not status:
        #     queryset = queryset.exclude(status="DELETE")

        return queryset

        # ordering = ('-id')

    # def list(self, request):
    #     queryset = User.objects.all().select_related('profile')
    #     serializer = UserSerializer(queryset, many=True)
    #
    #     # for item in serializer.data:
    #     #     # if item.profile.department:
    #     #     return HttpResponse(str(item))
    #
    #     content = {"code": 20000, "data": serializer.data}
    #     return Response(content)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        model_data = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(model_data)

        content = {"code": 20000, "data": serializer.data}
        return Response(content)

    def destroy(self, request, pk=None):
        User.objects.filter(id=pk).delete()
        content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)

    def create(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
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

# class UserRegistration(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def create(self, request):
#         data = request.data
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             content = {"code": 20000, "data": {"status": "success"}}
#         return Response(content)
