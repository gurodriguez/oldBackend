from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Category


class ProductSerializer(serializers.ModelSerializer):    
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True)

    class Meta:
        fields = ('id', 'name', 'sku', 'price', 'brand',
                  'image_url', 'category_id', 'category')
        model = Product
        depth = 1

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = CategorySerializer(instance.category).data
        return response
