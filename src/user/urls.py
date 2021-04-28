from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('log-in/', obtain_auth_token),
    path('log-out/', views.UserLogOutView.as_view()),
    path('details/', views.UserDetailView.as_view()),
]
