from rest_framework import serializers
from .models import Product, Category


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'slug',
            'image',
        ]
        

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'image',
            
        ]
        
class CategoryDetailSerializer(serializers.ModelSerializer):
    products= ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'image',
            'products',
        ]