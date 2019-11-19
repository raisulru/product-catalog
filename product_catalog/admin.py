from django.contrib import admin
from .models import ProductCatalog, ProductAttribute, ProductPrice


class ProductCatalogAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'code', 'available']
    search_ffields = ('name', 'slug', 'code')
    filter_fields = ['available']
admin.site.register(ProductCatalog, ProductCatalogAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['product', 'color', 'size']
    search_ffields = ('product', 'color')
admin.site.register(ProductAttribute, ProductAttributeAdmin)


class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'from_date', 'to_date']
    search_ffields = ('product', 'price')
admin.site.register(ProductPrice, ProductPriceAdmin)