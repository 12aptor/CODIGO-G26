from rest_framework import serializers
from .models import (
    SaleModel,
    SaleDetailModel,
    CustomerModel,
)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'

class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetailModel
        fields = '__all__'
        extra_kwargs = {
            'sale': {
                'required': False
            }
        }

class SaleSerializer(serializers.ModelSerializer):
    code = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    customer = CustomerSerializer()
    details = SaleDetailSerializer(many=True)

    class Meta:
        model = SaleModel
        fields = '__all__'

    def create(self, validated_data):
        customer = validated_data.pop('customer')
        details = validated_data.pop('details')

        customer, _ = CustomerModel.objects.get_or_create(**customer)
        sale = SaleModel.objects.create(customer=customer, **validated_data)

        for detail in details:
            SaleDetailModel.objects.create(sale=sale, **detail)
        
        return sale