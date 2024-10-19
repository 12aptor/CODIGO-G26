from django.urls import path
from .views import *


urlpatterns = [
    path('sales/create', CreateSaleView.as_view()),
]