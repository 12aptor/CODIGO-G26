from django.db import models
from warehouse.models import ProductModel


class CustomerModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    document_number = models.CharField(max_length=100)

    class Meta:
        db_table = 'customers'


class SaleModel(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    total = models.FloatField()

    STATUS_CHOICES = (
        ('PENDING', 'Pendiente'),
        ('COMPLETED', 'Completado'),
        ('CANCELLED', 'Cancelado'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(
        CustomerModel,
        on_delete=models.CASCADE,
        related_name='sales',
        db_column='customer_id'
    )

    class Meta:
        db_table = 'sales'


class SaleDetailModel(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    subtotal = models.FloatField()
    sale = models.ForeignKey(
        SaleModel,
        on_delete=models.CASCADE,
        related_name='details',
        db_column='sale_id',
    )
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='sale_details',
        db_column='product_id'
    )

    class Meta:
        db_table = 'sale_details'