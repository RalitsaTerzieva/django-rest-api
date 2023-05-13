import pytest
from django.test import TestCase

from  rest_framework.test import APIClient
from snippets.models import Snippet
from snippets.factories import UserFactory


@pytest.mark.django_db
class TestExampleTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        user = UserFactory.create()
        self.client.force_login(user=user)
        
    def test_create_snippet_should_return_http_created(self):
        data = {'code': 'print("Hello!")'}
        
        response = self.client.post('/snippets/', data=data)
        
        assert response.status_code == 201
        
    def test_create_snippet_should_create_snippet_object_correctly(self):
        data = {'code': 'print("Hello!")'}
        
        self.client.post('/snippets/', data=data)
        
        assert Snippet.objects.first().code == 'print("Hello!")'
