from django.db.utils import IntegrityError
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """."""

    password2 = serializers.CharField(write_only=True)

    class Meta:
        """."""

        model = User
        fields = ('id', 'email', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        """."""

        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError('Both the passwords should match')
        
        try:
            user = User.objects.get(email=validated_data['email'])
        except User.DoesNotExist:
            user = User(
                email=validated_data['email'],
                username=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
        else:
            raise serializers.ValidationError('User already exists')
