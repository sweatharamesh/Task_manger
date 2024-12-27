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

class TestGetTask(TestCase):
    def setUp(self):
        self.client = Client()
        self.get_url = reverse('get-task')
        Task.objects.create(title="Test Task", owner="Test Owner")

    def test_get_tasks(self):
        response = self.client.get(self.get_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['data']), 1)

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
