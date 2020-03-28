from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url

from .views import AppointmentSerialViewSet, AppointmentViewSet


app_name = "appointmentSerial"

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'appointment-serials', AppointmentSerialViewSet, basename='appointment-serial')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
urlpatterns = router.urls

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
