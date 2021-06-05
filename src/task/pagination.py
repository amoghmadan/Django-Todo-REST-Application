from rest_framework import pagination


class TaskPagination(pagination.PageNumberPagination):
    """Paginating Tasks with a Limit of 5"""

    page_size = 5
