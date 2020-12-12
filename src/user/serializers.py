from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """."""

    confirm_password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        """."""

        confirm_password = validated_data.pop('confirm_password')
        if validated_data['password'] != confirm_password:
            raise serializers.ValidationError('Both the passwords should match')

        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        """."""

        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
