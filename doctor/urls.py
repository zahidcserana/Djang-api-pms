from django.urls import path
from django.conf.urls import url

from .views import DoctorViewSet


app_name = "doctor"

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')
urlpatterns = router.urls
