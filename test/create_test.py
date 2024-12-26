from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task

class TestCreateTask(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('create-task')

    def test_create_task_valid(self):
        response = self.client.post(self.create_url, {
            'title': 'New Task',
            'owner': 'New Owner',
        })
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Task.objects.count(), 1)

    def test_create_task_invalid(self):
        response = self.client.post(self.create_url, {
            'title': '',
            'owner': 'New Owner',
        })
        self.assertEqual(response.status_code, 200)  
        self.assertIn("errors", response.context)
