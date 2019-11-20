import factory
from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = User

    email = 'admin@admin.com'
    username = 'admin'
    password = factory.PostGenerationMethodCall('set_password', '1234')

    is_superuser = True
    is_staff = True
    is_active = True
