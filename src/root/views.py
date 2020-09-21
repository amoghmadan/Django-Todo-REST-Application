from django import views
from django.shortcuts import render


class UserIndexView(views.View):
    """."""

    template_name = 'user/index.html'

    def get(self, request, *args, **kwargs):
        """."""

        return render(request, self.template_name)


class TodoIndexView(UserIndexView):
    """."""

    template_name = 'todo/index.html'
