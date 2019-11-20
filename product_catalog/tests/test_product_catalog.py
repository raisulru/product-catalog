from faker import Faker
from django.urls import reverse
from commons.test_cases import ProductTestCases
from product_catalog.tests import ProductCatalogFactory
from authentication.tests import UserFactory


class ProductListAPITest(ProductTestCases):
    url = reverse('product-list')
    login_url = reverse('access-token')
    fake = Faker()

    def setUp(self):
        user_obj = {
            'username': 'raisul',
            'password': '1234'
        }
        self.newuser = UserFactory(**user_obj)
        response = self.client.post(self.login_url, user_obj, format='json')
        self.token = response.data['access']
        super(ProductListAPITest, self).setUp()

    def test_product_list_get(self):
        # Request without login
        response = self.client.get(self.url)
        self.assertUnauthorized(response)

        ProductCatalogFactory.create_batch(5)

        # Request with login
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(self.url)
        self.assertSuccess(response)
        self.assertEqual(response.data['count'], 5)

    def test_product_post(self):
        data = {
            'name': 'Phone',
            'code': '123654'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        response = self.client.post(self.url, data, format='json')
        self.assertCreated(response)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['code'], data['code'])
