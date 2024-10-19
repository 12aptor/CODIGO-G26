from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import (
    SaleSerializer,
)
from drf_yasg.utils import swagger_auto_schema


SALE_TAG = 'Ventas'

class CreateSaleView(generics.CreateAPIView):
    serializer_class = SaleSerializer

    @swagger_auto_schema(tags=[SALE_TAG])
    def post(self, request, *args, **kwargs):
        """ Crear una venta (método POST) """
        response = super().post(request, *args, **kwargs)

        return Response({
            'message': 'Venta creada exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)