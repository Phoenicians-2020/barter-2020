import sys

from rest_framework import serializers

from products.models import Product, ProductPhoto


class ProductPhotoSerializer(serializers.ModelSerializer):
    """
    Product photo serializer class for creating product that has multiple photos
    """

    class Meta:
        model = ProductPhoto
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    """
    Product serializer class for creating product connected to an account
    """
    name = serializers.CharField()
    description = serializers.CharField()
    # product_type = serializers.IntegerField()

    class Meta:
        model = Product
        fields = (
            'name',
            'description'
        )

    def create(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        # product_type = validated_data.get('product_type')

        request = self.context.get('request')
        user = request.user
        profile = user.profile.get()

        product = Product(
            name=name,
            description=description,
            profile=profile
        )
        product.save()

        return product
