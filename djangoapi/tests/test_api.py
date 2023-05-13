import pytest
from django.test import TestCase

from  rest_framework.test import APIClient
from snippets.models import Snippet
from snippets.factories import SnippetFactory, UserFactory


@pytest.mark.django_db
class TestExampleTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory.create()
        self.client.force_login(user=self.user)
        
    def test_create_snippet_should_return_http_created(self):
        data = {'code': 'print("Hello!")'}
        
        response = self.client.post('/snippets/', data=data)
        
        assert response.status_code == 201
        
    def test_create_snippet_should_create_snippet_object_correctly(self):
        data = {'code': 'print("Hello!")'}
        
        self.client.post('/snippets/', data=data)
        
        assert Snippet.objects.first().code == 'print("Hello!")'
        
        
    def test_update_snippet_should_update_snippet_object_correctly(self):
        data = {'code': 'print("Hello World forever!")'}
        SnippetFactory.create(pk=1, owner=self.user)
        
        self.client.put('/snippets/1/', data=data)
        
        assert Snippet.objects.first().code == 'print("Hello World forever!")'
        
