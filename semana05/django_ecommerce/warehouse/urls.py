from django.urls import path
from .views import *


urlpatterns = [
    path('categories/list', ListCategoryView.as_view()),
    path('categories/create', CreateCategoryView.as_view()),
    path('categories/update/<int:pk>', UpdateCategoryView.as_view()),
    path('categories/delete/<int:pk>', DeleteCategoryView.as_view()),

    path('products/list', ListProductView.as_view()),
    path('products/list/active', ListActiveProductView.as_view()),
    path('products/search/<str:name>', SearchProductView.as_view()),
    path('products/create', CreateProductView.as_view()),
    path('products/update/<int:pk>', UpdateProductView.as_view()),
    path('products/delete/<int:pk>', DeleteProductView.as_view()),
]