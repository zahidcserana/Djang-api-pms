from django.urls import path
from django.conf.urls import url

from . import views
from .views import PatientViewSet

app_name = "patient"

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
urlpatterns = router.urls

urlpatterns += [
    path('patient-search/', views.PatientSearchView.as_view()),
]
