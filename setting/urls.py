from rest_framework import routers
from .views import DepartmentViewSet, UserInfo
from django.urls import path

app_name = "setting"


router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
# urlpatterns = router.urls

urlpatterns = [
    path('users/info/', UserInfo.as_view(), name='info'),
]
