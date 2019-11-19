from rest_framework import viewsets
from .models import ProductCatalog, ProductAttribute, ProductPrice
from .serializers import ProductCatalogSerializer, ProductAttributeSerializer, ProductPriceSerializer


class ProductCatalogView(viewsets.ModelViewSet):
	serializer_class = ProductCatalogSerializer
	queryset = ProductCatalog.objects.all()
	lookup_field = 'slug'