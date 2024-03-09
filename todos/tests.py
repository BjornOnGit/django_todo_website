""" The beginning of the test suite for the todos app."""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo

class TodoModelTest(TestCase):
    """ Test the Todo model. """
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title='First Todo',
            body='A body of text here'
        )

    def test_model_content(self):
        """Test that the Todo model has the correct fields."""
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "A body of text here")
        self.assertEqual(str(self.todo), "First Todo")
    
    def test_api_listview(self):
        """Test that the API list view returns the correct data."""
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)
    
    def test_api_detailview(self):
        """Test that the API detail view returns the correct data."""
        response = self.client.get(
            reverse('todo_detail', kwargs={'pk': self.todo.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, 'First Todo')

# Create your tests here.
