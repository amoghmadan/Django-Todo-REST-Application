from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer


class UserRegisterView(generics.CreateAPIView):
    """."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailView(generics.RetrieveAPIView):
    """."""

    serializer_class = UserSerializer

    def get_object(self):
        """."""

        return self.request.user


class UserLogOutView(generics.DestroyAPIView):
    """."""

    queryset = Token.objects.all()

    def get_object(self):
        """."""

        return self.queryset.get(user=self.request.user)
