from django.urls import path
from django.conf.urls import url

from .views import AppointmentSerialViewSet


app_name = "appointmentSerial"

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'appointment-serials', AppointmentSerialViewSet, basename='appointment-serial')
urlpatterns = router.urls
