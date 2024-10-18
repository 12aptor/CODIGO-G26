from django.urls import path
from .views import *


urlpatterns = [
    path('categories/list', ListCategoryView.as_view()),
    path('categories/create', CreateCategoryView.as_view()),
    path('categories/update/<int:pk>', UpdateCategoryView.as_view()),
    path('categories/delete/<int:pk>', DeleteCategoryView.as_view()),

    path('products/list', ListProductView.as_view()),
]