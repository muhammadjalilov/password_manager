from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.password_manage.models import PasswordManage
from apps.password_manage.serializers import PasswordManageSerializer, PasswordManageListSerializer


class PasswordManageViewSet(ModelViewSet):
    queryset = PasswordManage.objects.all()
    serializer_class = PasswordManageSerializer
    http_method_names = ['get', 'post', 'delete', 'put']

    def get_queryset(self):
        return self.queryset.filter(account=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return PasswordManageListSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)
