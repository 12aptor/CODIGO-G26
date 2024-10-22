from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    SaleSerializer,
)
from drf_yasg.utils import swagger_auto_schema
import os
import requests


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
    

class InvoiceView(APIView):

    @swagger_auto_schema(tags=[SALE_TAG])
    def post(self, request):
        """ Generar factura (método POST) """
        try:
            item = {
                'unidad_de_medida': 'NIU',
                'codigo': 'C0001',
                'descripcion': 'Producto 1',
                'cantidad': 1,
                'valor_unitario': 100,
                'precio_unitario': 118,
                'subtotal': 100,
                'tipo_de_igv': 1,
                'igv': 18,
                'total': 118,
                'anticipo_regularizacion': False,
            }

            invoice_data = {
                'operacion': 'generar_comprobante',
                'tipo_de_comprobante': 2,
                'serie': 'BBB1',
                'numero': 1,
                'sunat_transaction': 1,
                'cliente_tipo_de_documento': 1,
                'cliente_numero_de_documento': '00000000',
                'cliente_denominacion': 'Cliente de prueba',
                'cliente_direccion': 'Avenida los Girasoles 123',
                'cliente_email': 'email@email.com',
                'fecha_de_emision': '21-10-2024',
                'moneda': 1,
                'porcentaje_de_igv': 18.00,
                'total_gravada': 100.00,
                'total_igv': 18.00,
                'total': 118.00,
                'enviar_automaticamente_a_la_sunat': True,
                'enviar_automaticamente_al_cliente': True,
                'items': [
                    item
                ]
            }

            api_url = os.getenv('NUBEFACT_API')
            token = os.getenv('NUBEFACT_TOKEN')

            nubefact_response = requests.post(
                url=api_url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {token}',
                },
                json=invoice_data
            )

            nubefact_response_json = nubefact_response.json()
            nubefact_response_status = nubefact_response.status_code

            if nubefact_response_status != 200:
                raise Exception(nubefact_response_json['errors'])

            return Response({
                'message': 'Factura generada exitosamente',
                'data': nubefact_response_json
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Error al generar factura',
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @swagger_auto_schema(tags=[SALE_TAG])
    def get(self, request):
        """ Consultar facturas (método GET) """
        try:
            api_url = os.getenv('NUBEFACT_API')
            token = os.getenv('NUBEFACT_TOKEN')

            invoice_data = {
                'operacion': 'consultar_comprobante',
                'tipo_de_comprobante': 2,
                'serie': 'BBB1',
                'numero': 1,
            }

            nubefact_response = requests.post(
                url=api_url,
                headers={
                    'Authorization': f'Bearer {token}',
                },
                json=invoice_data
            )

            nubefact_response_json = nubefact_response.json()
            nubefact_response_status = nubefact_response.status_code

            if nubefact_response_status != 200:
                raise Exception(nubefact_response_json['errors'])

            return Response({
                'message': 'Factura consultada exitosamente',
                'data': nubefact_response_json
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Error al consultar facturas',
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
