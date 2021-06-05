from django.db.models import QuerySet
from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer
from .filters import TaskFilterSet
from .pagination import TaskPagination


class TaskViewSet(viewsets.ModelViewSet):
    """CRUD operation around Task Model"""

    queryset = Task.objects.order_by('-created_at')
    serializer_class = TaskSerializer
    filterset_class = TaskFilterSet
    pagination_class = TaskPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Get the list of items for this view.
        This must be an iterable, and may be a queryset.
        Defaults to using `self.queryset`.

        This method should always be used rather than accessing `self.queryset`
        directly, as `self.queryset` gets evaluated only once, and those results
        are cached for all subsequent requests.

        You may want to override this if you need to provide different
        querysets depending on the incoming request.

        (Eg. return a list of items that is specific to the user)
        """
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset.filter(user=self.request.user)
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset
