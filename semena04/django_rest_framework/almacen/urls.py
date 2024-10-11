from django.urls import path
from .views import (
    ListProductCategoryView,
    CreateProductCategoryView,
)


urlpatterns = [
    path('product_categories/list', ListProductCategoryView.as_view()),
    path('product_categories/create', CreateProductCategoryView.as_view()),
]