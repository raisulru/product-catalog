from django.urls import path
from .views import ProductCatalogView, ProductPriceView, ProductAttributeView

urlpatterns = [
    path('products/', ProductCatalogView.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('products/<slug>/prices', ProductPriceView.as_view({'get': 'list', 'post': 'create'}), name='product-price-list'),
    path('products/<slug>/attributes', ProductPriceView.as_view({'get': 'list', 'post': 'create'}), name='product-attribute-list'),
    path('products/<slug>/', ProductCatalogView.as_view({'get': 'retrieve', 'put': 'update'}), name='product-details')
]