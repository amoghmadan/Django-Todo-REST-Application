from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet, UserLogOutView, UserDetailsView

router = routers.DefaultRouter()
router.register(r'register', UserViewSet)

urlpatterns = [
    path('log-in/', obtain_auth_token),
    path('log-out/', UserLogOutView.as_view()),
    path('details/', UserDetailsView.as_view()),
]

urlpatterns += router.urls
