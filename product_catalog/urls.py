from django.urls import path
from .views import ProductCatalogView

urlpatterns = [
    path('products/', ProductCatalogView.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('products/<slug>/', ProductCatalogView.as_view({'get': 'retrieve', 'put': 'update'}), name='product-details')
]