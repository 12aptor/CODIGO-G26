from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
)
from utils.pagination import Pagination
from django.http import Http404
from .models import (
    CategoryModel,
    ProductModel
)
from .serializers import (
    CategorySerializer,
    ProductSerializer,
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from authentication.permissions import (
    IsAuthenticated,
    IsAdmin,
    IsSellerOrAdmin,
)

CATEGORY_TAG = 'Categoria de productos'
PRODUCT_TAG = 'Productos'

class ListCategoryView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(tags=[CATEGORY_TAG])
    def get(self, request, *args, **kwargs):
        """ Listar categorias (método GET) """
        response = super().get(request, *args, **kwargs)

        return Response({
            'message': 'Categorias listadas exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class CreateCategoryView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(tags=[CATEGORY_TAG])
    def post(self, request, *args, **kwargs):
        """ Crear una categoria (método POST) """
        response = super().post(request, *args, **kwargs)

        return Response({
            'message': 'Categoria creada exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class UpdateCategoryView(generics.UpdateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(tags=[CATEGORY_TAG])
    def put(self, request, *args, **kwargs):
        """ Actualiza una categoria (método PUT) """
        try:
            response = super().put(request, *args, **kwargs)

            return Response({
                'message': 'Categoria actualizada exitosamente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Categoria no encontrada',
            }, status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(tags=[CATEGORY_TAG])
    def patch(self, request, *args, **kwargs):
        """ Actualiza parcialmente una categoria (método PATCH) """
        try:
            response = super().partial_update(request, *args, **kwargs)

            return Response({
                'message': 'Categoria actualizada exitosamente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Categoria no encontrada',
            }, status=status.HTTP_404_NOT_FOUND)
    
class DeleteCategoryView(generics.DestroyAPIView):
    queryset = CategoryModel.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    
    @swagger_auto_schema(tags=[CATEGORY_TAG])
    def delete(self, request, *args, **kwargs):
        try:
            category = self.get_object()
            category.status = False
            category.save()

            return Response({
                'message': 'Categoria eliminada exitosamente',
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Categoria no encontrada',
            }, status=status.HTTP_404_NOT_FOUND)

class ListProductView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticated, IsSellerOrAdmin]

    @swagger_auto_schema(tags=[PRODUCT_TAG])
    def get(self, request, *args, **kwargs):
        """ Listar productos (método GET) """
        response = super().get(request, *args, **kwargs)

        return Response({
            'message': 'Productos listados exitosamente',
            'data': response.data['results'],
            'count': response.data['count'],
            'next': response.data['next'],
            'previous': response.data['previous'],
        }, status=status.HTTP_200_OK)
    
class ListActiveProductView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return super().get_queryset().filter(status='ACTIVE').order_by('id')
    
    @swagger_auto_schema(tags=[PRODUCT_TAG])
    def get(self, request, *args, **kwargs):
        """ Listar productos (método GET) """
        response = super().get(request, *args, **kwargs)

        return Response({
            'message': 'Productos listados exitosamente',
            'data': response.data['results'],
            'count': response.data['count'],
            'next': response.data['next'],
            'previous': response.data['previous'],
        }, status=status.HTTP_200_OK)
    
class SearchProductView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = Pagination

    def get_queryset(self):
        queryset = ProductModel.objects.filter(name__icontains=self.kwargs['name']).order_by('id')
        return queryset
    
    @swagger_auto_schema(tags=[PRODUCT_TAG])
    def get(self, request, *args, **kwargs):
        """ Buscar productos por el nombre (método GET) """
        response = super().get(request, *args, **kwargs)

        return Response({
            'message': 'Productos listados exitosamente',
            'data': response.data['results'],
            'count': response.data['count'],
            'next': response.data['next'],
            'previous': response.data['previous'],
        }, status=status.HTTP_200_OK)

class CreateProductView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    parser_classes = (MultiPartParser, FormParser)

    image_param = openapi.Parameter(
        'image',
        openapi.IN_FORM,
        description='Imagen del producto',
        type=openapi.TYPE_FILE,
        required=True,
    )

    @swagger_auto_schema(
        tags=[PRODUCT_TAG],
        manual_parameters=[image_param],
        consumes=['multipart/form-data']
    )
    def post(self, request, *args, **kwargs):
        """ Crear un producto (método POSt) """
        response = super().post(request, *args, **kwargs)

        return Response({
            'message': 'Producto creado exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class UpdateProductView(generics.UpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    parser_classes = (MultiPartParser, FormParser)

    image_param = openapi.Parameter(
        'image',
        openapi.IN_FORM,
        description='Imagen del producto',
        type=openapi.TYPE_FILE,
        required=False,
    )

    @swagger_auto_schema(
        tags=[PRODUCT_TAG],
        manual_parameters=[image_param],
        consumes=['multipart/form-data']
    )
    def put(self, request, *args, **kwargs):
        """ Actualiza un producto (método PUT) """
        try:
            response = super().put(request, *args, **kwargs)

            return Response({
                'message': 'Producto actualizado exitosamente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Producto no encontrado',
            }, status=status.HTTP_404_NOT_FOUND)
        
    @swagger_auto_schema(
        tags=[PRODUCT_TAG],
        manual_parameters=[image_param],
        consumes=['multipart/form-data']
    )
    def patch(self, request, *args, **kwargs):
        """ Actualiza parcialmente un producto (método PATCH) """
        try:
            response = super().partial_update(request, *args, **kwargs)

            return Response({
                'message': 'Producto actualizado exitosamente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Producto no encontrado',
            }, status=status.HTTP_404_NOT_FOUND)

class DeleteProductView(generics.DestroyAPIView):
    queryset = ProductModel.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin)

    @swagger_auto_schema(tags=[PRODUCT_TAG])
    def delete(self, request, *args, **kwargs):
        try:
            product = self.get_object()
            product.status = 'DELETED'
            product.save()

            return Response({
                'message': 'Producto eliminado exitosamente',
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Producto no encontrado',
            }, status=status.HTTP_404_NOT_FOUND)
