from django.db.models import QuerySet
from rest_framework import authentication, permissions, viewsets
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """."""

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        """Get User specific Todos ordered by Created At"""

        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset.filter(user=self.request.user).order_by('-created_at')
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset
