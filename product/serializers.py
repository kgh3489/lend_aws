from .models import CommentModel, ProductModel
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    #author = serializers.ReadOnlyField(source = 'user.username')

    class Meta:
        model = CommentModel
        fields = [
            'id',
            'product',
            'author',
            'comment',
            'created_at'
            ]

class ProductSerializer(serializers.ModelSerializer):
    product_img = serializers.ImageField(use_url=True)
    comments = CommentSerializer(many=True, read_only=True)
    #author = serializers.ReadOnlyField(source = 'user.username')

    class Meta:
        model = ProductModel
        fields = (
            'id',
            'author',
            'product_img',
            'product_name',
            'product_type',
            'product_lend_h',
            'product_lend_d',
            'product_location',
            'product_detail',
            'comments'
            ) # 필드 설정
