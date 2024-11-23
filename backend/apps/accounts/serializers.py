from rest_framework import serializers

from apps.accounts.models import Account


class RegisterSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'password', 'password_confirmation', 'first_name', 'last_name', 'email']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = super().create(validated_data)
        instance.set_password(password)
        instance.save()
        return instance
