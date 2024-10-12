from django.urls import path
from .views import (
    ListProductCategoryView,
    CreateProductCategoryView,
    UpdateProductCategoryView,
    DeleteProductCategoryView,
    RetrieveProductCategoryView,
)


urlpatterns = [
    path('product_categories/list', ListProductCategoryView.as_view()),
    path('product_categories/create', CreateProductCategoryView.as_view()),
    path('product_categories/update/<int:pk>', UpdateProductCategoryView.as_view()),
    path('product_categories/delete/<int:pk>', DeleteProductCategoryView.as_view()),
    path('product_categories/<int:pk>', RetrieveProductCategoryView.as_view())
]