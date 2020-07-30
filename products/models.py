from django.db import models

from users.models import Profile

optional = {
    'null': True,
    'blank': True
}


class ProductPhoto(models.Model):
    profile_photo = models.ImageField(upload_to='product_images/', **optional)


class ProductType(models.Model):
    name = models.CharField(max_length=255, **optional)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=255, **optional)
    description = models.CharField(max_length=255, **optional)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="products")
    product_photo = models.ForeignKey(ProductPhoto, on_delete=models.CASCADE, related_name="products", **optional)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="products", **optional)

    def __str__(self):
        return self.name
