from django.contrib import admin
from .models import ProductModel, ProductCategoryModel


class ProductsInline(admin.TabularInline):
    model = ProductModel
    extra = 1
    readonly_fields = ('name', 'price', 'status', 'created_at', 'updated_at')

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'created_at')
    search_fields = ('name', 'product_category__name')
    list_per_page = 10

admin.site.register(ProductModel, ProductModelAdmin)

class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)
    list_per_page = 10
    inlines = [ProductsInline]

admin.site.register(ProductCategoryModel, ProductCategoryModelAdmin)