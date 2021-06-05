from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    """Registering new user"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class DetailView(generics.RetrieveAPIView):
    """Retrieving current user details"""

    serializer_class = UserSerializer

    def get_object(self):
        """Returning logged in user"""

        return self.request.user


class LogOutView(generics.DestroyAPIView):
    """Log out current user"""

    queryset = Token.objects.all()

    def get_object(self):
        """Retrieving current token to delete"""

        return self.queryset.get(user=self.request.user)
