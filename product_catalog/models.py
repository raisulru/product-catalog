from django.db import models


class ProductCatalog(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    code = models.CharField(max_length=30, null=True, blank=True)
    color = models.CharField(max_length=30)
    available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "product_catalog"
        verbose_name_plural = "Products Catalog"