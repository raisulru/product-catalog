import datetime

from django.db import models
from django.utils.text import slugify


class ProductCatalog(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False)
    code = models.CharField(max_length=30, null=True, blank=True)
    available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.slug)

    def save(self, *args, **kwargs):
        if not self.id:
            value = self.name + str(datetime.datetime.timestamp(datetime.datetime.now()))
            self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


    class Meta:
        db_table = "product_catalog"
        verbose_name_plural = "Products Catalog"


class ProductAttribute(models.Model):
    product = models.ForeignKey(ProductCatalog, on_delete=models.CASCADE, related_name='product_attributes')
    color = models.CharField(max_length=30, null=True, blank=True)
    size = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.product)


    class Meta:
        db_table = "product_attribute"
        verbose_name_plural = "Product Attributes"


class ProductPrice(models.Model):
    product = models.ForeignKey(ProductCatalog, on_delete=models.CASCADE, related_name='product_prices')
    price = models.PositiveIntegerField(default=0)
    from_date = models.DateTimeField(default=datetime.datetime.now)
    to_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.product)


    class Meta:
        db_table = "product_price"
        verbose_name_plural = "Product Prices"
