from django.db import models
from cloudinary.models import CloudinaryField


class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    price = models.FloatField()
    stock = models.IntegerField()

    STATUS_CHOICES = (
        ('ACTIVE', 'Activo'),
        ('INACTIVE', 'Inactivo'),
        ('DELETED', 'Eliminado'),
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ACTIVE'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name='products',
        db_column='category_id',
    )