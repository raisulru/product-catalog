from rest_framework import serializers
from .models import ProductCatalog, ProductAttribute, ProductPrice


class ProductAttributeSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductAttribute
		fields = [
			'id',
			'product',
			'color',
			'size'
		]

		read_only_fields = ['id', 'product']


class ProductPriceSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductPrice
		fields = [
			'id',
			'product',
			'price',
			'from_date',
			'to_date'
		]

		read_only_fields = ['id', 'product']


class ProductCatalogSerializer(serializers.ModelSerializer):
	product_attributes = ProductAttributeSerializer(many=True, read_only=True)
	product_prices = ProductPriceSerializer(many=True, read_only=True)

	class Meta:
		model = ProductCatalog
		fields = [
			'id',
			'name',
			'slug',
			'available',
			'product_attributes',
			'product_prices',
			'code',
			'description'
		]

		read_only_fields = ['id']

