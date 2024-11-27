from rest_framework import serializers

from apps.password_manage.models import PasswordManage
from apps.password_manage.utils import shifr, deshifr


class PasswordManageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordManage
        fields = ("id", 'site_name')


class PasswordManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordManage
        exclude = ('account',)

    def create(self, validated_data):
        validated_data["password"] = shifr(key=self.context["request"].user.password, passwd=validated_data["password"])
        return super().create(validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["password"] = deshifr(key=self.context["request"].user.password, passwd=data["password"])
        return data
