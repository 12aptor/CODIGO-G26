from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('roles/create', CreateRoleView.as_view()),
    path('roles/list', ListRoleView.as_view()),

    path('users/create', CreateUserView.as_view()),
    path('users/update/<int:pk>', UpdateUserView.as_view()),
    path('users/list', ListUserView.as_view()),

    path('auth/login', LoginView.as_view()),
    path('auth/refresh', TokenRefreshView.as_view()),
]