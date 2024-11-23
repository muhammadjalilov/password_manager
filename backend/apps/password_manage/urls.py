from rest_framework.routers import DefaultRouter

from apps.password_manage.views import PasswordManageViewSet

router = DefaultRouter()
router.register(r'', viewset=PasswordManageViewSet, basename='password_manage')
urlpatterns = router.urls