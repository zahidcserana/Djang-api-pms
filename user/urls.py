from django.urls import path
from django.conf.urls import url

from .views import UserViewSet
from .views import UserView


app_name = "users"

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# urlpatterns = [
#     # url(r'^users', UserViewSet),
#     # path('users/hello/', HelloView.as_view(), name='hello'),
#     # path('user/info/', UserInfo.as_view(), name='info'),
# ]