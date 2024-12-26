from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task

class TestUpdateTask(TestCase):
    def setUp(self):
        self.client = Client()
        self.update_url = reverse('update-task')
        self.task = Task.objects.create(title="Test Task", owner="Test Owner")

    def test_update_task_valid(self):
        response = self.client.post(self.update_url, {
            'id': self.task.id,
            'title': 'Updated Task',
            'owner': 'Updated Owner',
        })
        self.assertEqual(response.status_code, 302)  
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.owner, 'Updated Owner')

    def test_update_task_invalid(self):
        response = self.client.post(self.update_url, {
            'id': self.task.id,
            'title': '',
            'owner': '',
        })
        self.assertEqual(response.status_code, 200)  
        self.task.refresh_from_db()
        self.assertNotEqual(self.task.title, '')
        self.assertNotEqual(self.task.owner, '')
