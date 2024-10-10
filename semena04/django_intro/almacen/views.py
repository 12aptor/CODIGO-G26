from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ProductModel
import datetime


def home(request):
    return HttpResponse('Hola Django 👻')


def horario(request):
    now = datetime.datetime.now()
    html = f'<html><body>Ahora es: {now}</body></html>'
    return HttpResponse(html)

def json(request):
    data = {
        'Framework': 'Django'
    }
    return JsonResponse(data)

def producto(request, id):
    product = ProductModel.objects.get(id=id)
    print(product)
    return render(request, 'producto.html', context={'name': product.name})