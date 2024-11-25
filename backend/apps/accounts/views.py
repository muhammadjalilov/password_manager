from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.accounts.models import Account
from apps.accounts.serializers import RegisterSerializer


class RegisterViewSet(mixins.CreateModelMixin,
                      GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
