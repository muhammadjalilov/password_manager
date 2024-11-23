from rest_framework import serializers

from apps.password_manage.models import PasswordManage


class PasswordManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordManage
        exclude = ('account',)

