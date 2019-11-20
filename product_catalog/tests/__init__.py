import factory
from ..models import ProductCatalog


class ProductCatalogFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ProductCatalog

    name = factory.Faker('name')
    code = '1234ksad'
    available = True