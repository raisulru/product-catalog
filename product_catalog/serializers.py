from rest_framework import serializers
from .models import ProductCatalog, ProductAttribute, ProductPrice


class ProductCatalogSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductCatalog
		fields = [
			'id',
			'name',
			'slug',
			'available',
			'code',
			'description'
		]

		read_only_fields = ['id']


class ProductAttributeSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductAttribute
		fields = [
			'id',
			'product',
			'color',
			'size'
		]

		read_only_fields = ['id']


class ProductPriceSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductPrice
		fields = [
			'id',
			'price',
			'from_date',
			'to_date'
		]

		read_only_fields = ['id']
