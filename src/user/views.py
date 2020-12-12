from django.contrib.auth.models import User
from rest_framework import permissions, status, views, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post']


class UserDetailView(views.APIView):
    """."""

    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        """."""

        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserLogOutView(views.APIView):
    """."""

    model = Token

    def delete(self, request, *args, **kwargs):
        """."""

        token = self.model.objects.get(user=request.user)
        token.delete()
        return Response({'detail': 'Logged Out Successfully'}, status.HTTP_204_NO_CONTENT)
