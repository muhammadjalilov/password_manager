from rest_framework.routers import DefaultRouter

from apps.accounts.views import RegisterViewSet

router = DefaultRouter()
router.register(r'', viewset=RegisterViewSet, basename='register')
urlpatterns = router.urls
