from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('log-in/', obtain_auth_token),
    path('details/', views.DetailView.as_view()),
    path('log-out/', views.LogOutView.as_view()),
]
