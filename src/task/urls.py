from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views, viewsets

router = DefaultRouter()
router.register('tasks', viewsets.TaskViewSet)

urlpatterns = [
    path('status-choice/', views.TaskStatusChoiceView.as_view()),
]

urlpatterns += router.urls
