from rest_framework import generics, status
from rest_framework.response import Response
from .models import ProductCategoryModel
from .serializers import ProductCategorySerializer


class ListProductCategoryView(generics.ListAPIView):
    # queryset = ProductCategoryModel.objects.all()
    serializer_class = ProductCategorySerializer

    def get_queryset(self):
        product_categories = ProductCategoryModel.objects.filter(status='ACTIVE')
        # product_categories = self.queryset.filter(status='ACTIVE')
        return product_categories

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Product categories fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

class CreateProductCategoryView(generics.CreateAPIView):
    serializer_class = ProductCategorySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'message': 'Product category created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)