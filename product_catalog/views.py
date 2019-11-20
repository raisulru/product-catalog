from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from .models import (
	ProductCatalog, 
	ProductAttribute, 
	ProductPrice
)
from .serializers import (
	ProductCatalogSerializer, 
	ProductAttributeSerializer, 
	ProductPriceSerializer
)


class ProductCatalogView(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]
	serializer_class = ProductCatalogSerializer
	lookup_field = 'slug'

	def get_queryset(self):
		queryset = ProductCatalog.objects.filter(available=True)
		return queryset


class ProductAttributeView(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]
	serializer_class = ProductAttributeSerializer
	lookup_field = 'slug'

	def get_queryset(self):
		product_slug = self.kwargs.get('slug')
		queryset = ProductAttribute.objects.filter(product__slug=product_slug)
		return queryset

	def create(self, request, *args, **kwargs):
		product_slug = self.kwargs.get('slug')

		try:
			product = ProductCatalog.objects.get(slug=product_slug)
		except ProductPrice.DoesNotExist:
			return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

		serializer = ProductAttributeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(product=product)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductPriceView(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]
	serializer_class = ProductPriceSerializer
	lookup_field = 'slug'

	def get_queryset(self):
		product_slug = self.kwargs.get('slug')
		queryset = ProductPrice.objects.filter(product__slug=product_slug)
		return queryset

	def create(self, request, *args, **kwargs):
		product_slug = self.kwargs.get('slug')

		try:
			product = ProductCatalog.objects.get(slug=product_slug)
		except ProductPrice.DoesNotExist:
			return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

		serializer = ProductPriceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(product=product)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
