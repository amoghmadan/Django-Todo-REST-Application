from rest_framework import pagination


class TaskPagination(pagination.PageNumberPagination):
    """."""

    page_size = 25
