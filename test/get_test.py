from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task

class TestGetTask(TestCase):
    def setUp(self):
        self.client = Client()
        self.get_url = reverse('get-task')
        Task.objects.create(title="Test Task", owner="Test Owner")

    def test_get_tasks(self):
        response = self.client.get(self.get_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['data']), 1)
