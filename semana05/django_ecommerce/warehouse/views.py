from rest_framework import generics, status
from rest_framework.response import Response
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

    page_param = openapi.Parameter(
        'page',
        openapi.IN_QUERY,
        type=openapi.TYPE_INTEGER,
        description='Número de página',
    )
    per_page_param = openapi.Parameter(
        'per_page',
        openapi.IN_QUERY,
        type=openapi.TYPE_INTEGER,
        description='Número de productos por página',
    )

    def get_queryset(self):
        return super().get_queryset()

    @swagger_auto_schema(tags=[PRODUCT_TAG], manual_parameters=[page_param, per_page_param])
    def get(self, request, *args, **kwargs):
        """ Listar productos (método GET) """
        response = super().get(request, *args, **kwargs)

        return Response({
            'message': 'Productos listados exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)
