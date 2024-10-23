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
    
    def validate(self, attrs):
        # Validar el stock de cada producto
        details = attrs.get('details')

        for detail in details:
            product = detail.get('product')
            if product.stock < detail.get('quantity'):
                raise serializers.ValidationError(
                    f'No hay suficiente stock de {product.name}'
                )

        return attrs

    def create(self, validated_data):
        customer = validated_data.pop('customer')
        details = validated_data.pop('details')
        customer, _ = CustomerModel.objects.get_or_create(
            document_number=customer.get('document_number'),
            defaults=customer
        )
        # try:
        #     customer = CustomerModel.objects.get(
        #         document_number=customer.get('document_number')
        #     )
        # except CustomerModel.DoesNotExist:
        #     customer = CustomerModel.objects.create(**customer)
        sale = SaleModel.objects.create(customer=customer, **validated_data)

        for detail in details:
            # Restar el stock de cada producto
            product = detail.get('product')
            quantity = detail.get('quantity')
            if product.stock < quantity:
                raise serializers.ValidationError(
                    f'No hay suficiente stock de {product.name}'
                )
            product.stock -= quantity
            product.save()

            SaleDetailModel.objects.create(sale=sale, **detail)
        
        return sale