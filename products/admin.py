from django.contrib import admin

from products.models import (
    Product,
    ProductPhoto,
    ProductType
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "profile",
        "product_type"
    ]
    search_fields = ["name"]


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name"
    ]
    search_fields = ["name"]
