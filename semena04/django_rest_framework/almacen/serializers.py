from rest_framework import serializers
from .models import ProductCategoryModel


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategoryModel
        fields = '__all__'
        # fields = ('id', 'name', 'status')
        # exclude = ('id',)
        # read_only_fields = ('id',)