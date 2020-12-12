from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = DefaultRouter()
router.register('register', views.UserViewSet)

urlpatterns = [
    path('log-in/', obtain_auth_token),
    path('log-out/', views.UserLogOutView.as_view()),
    path('details/', views.UserDetailView.as_view()),
]

urlpatterns += router.urls
