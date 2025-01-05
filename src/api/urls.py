from api.views import FishViewSet, PlantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'fish', FishViewSet)
router.register(r'plants', PlantViewSet)

urlpatterns = router.urls