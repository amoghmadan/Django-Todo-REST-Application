from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User Model Serializer"""

    confirm_password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        """Popping out the confirm password field and validating it"""

        confirm_password = validated_data.pop('confirm_password')
        if validated_data['password'] != confirm_password:
            raise serializers.ValidationError('Both the passwords should match')

        return super(UserSerializer, self).create(validated_data)

    class Meta:
        """Configuring the 'password' field to be write only"""

        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
