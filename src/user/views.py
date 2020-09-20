from rest_framework import authentication, permissions, response, status, views, viewsets
from .models import User, Token
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']


class UserLogOutView(views.APIView):
    """."""

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """."""

        token = Token.objects.get(user=request.user)
        token.delete()

        return response.Response({}, status=status.HTTP_200_OK)


class UserDetailsView(views.APIView):
    """."""

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """."""

        serializer = self.serializer_class(request.user)

        return response.Response(serializer.data, status=status.HTTP_200_OK)
