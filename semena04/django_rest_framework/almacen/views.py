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
        # print("search params: ", request.GET.get('page'))

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
    
class UpdateProductCategoryView(generics.UpdateAPIView):
    queryset = ProductCategoryModel.objects.all()
    serializer_class = ProductCategorySerializer

    def update(self, request, *args, **kwargs):
        # print("pk: ", kwargs.get('pk'))

        response = super().update(request, *args, **kwargs)

        return Response({
            'message': 'Product category updated successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class DeleteProductCategoryView(generics.DestroyAPIView):
    queryset = ProductCategoryModel.objects.all()
    serializer_class = ProductCategorySerializer

    def destroy(self, request, *args, **kwargs):
        product_category = self.get_object()
        product_category.status = 'DELETED'
        product_category.save()

        serializer = self.get_serializer(product_category)

        return Response({
            'message': 'Product category deleted successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class RetrieveProductCategoryView(generics.RetrieveAPIView):
    queryset = ProductCategoryModel.objects.all()
    serializer_class = ProductCategorySerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)

        return Response({
            'message': 'Product category fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)