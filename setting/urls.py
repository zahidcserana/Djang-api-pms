from .views import DepartmentViewSet

app_name = "setting"

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
urlpatterns = router.urls


