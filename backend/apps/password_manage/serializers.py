from rest_framework import serializers

from apps.password_manage.models import PasswordManage

class PasswordManageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordManage
        fields = ("id",'site_name')
class PasswordManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordManage
        exclude = ('account',)

