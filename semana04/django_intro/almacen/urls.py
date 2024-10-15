from django.urls import path
from .views import home, horario, json, producto

urlpatterns = [
    path('inicio', home, name='home'),
    path('horario', horario, name='horario'),
    path('json', json, name='json'),
    path('producto/<int:id>', producto, name='producto'),
]