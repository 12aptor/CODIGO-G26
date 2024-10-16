from django.urls import path
from .views import *


urlpatterns = [
    path('roles/create', CreateRoleView.as_view()),
    path('roles/list', ListRoleView.as_view()),

    path('users/create', CreateUserView.as_view()),
]