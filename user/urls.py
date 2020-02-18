from django.urls import path
from django.conf.urls import url

from .views import UserViewSet, HelloView
from .views import UserView


app_name = "users"

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls


# urlpatterns = [
#     # path('user_view/<int:pk>', UserView.as_view())
#     url(r'^users', UserViewSet),
#     # path('users/hello/', HelloView.as_view(), name='hello'),
# ]