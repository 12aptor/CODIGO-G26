# Generated by Django 5.1.2 on 2024-10-10 00:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('ACTIVE', 'Activo'), ('INACTIVE', 'Inactivo'), ('DELETED', 'Eliminado')], max_length=10)),
            ],
            options={
                'db_table': 'product_categories',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('status', models.BooleanField(default=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_category', models.ForeignKey(db_column='product_category_id', on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='almacen.productcategorymodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
    ]
