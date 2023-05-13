import factory
from django.contrib.auth.models import User
from .models import Snippet


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.PostGenerationMethodCall('set_password', 'password')


class SnippetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Snippet