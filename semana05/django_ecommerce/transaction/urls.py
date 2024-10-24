from django.urls import path
from .views import *


urlpatterns = [
    path('sales/create', CreateSaleView.as_view()),
    path('sales/list', ListSaleView.as_view()),
    
    path('sales/invoice', InvoiceView.as_view()),
]