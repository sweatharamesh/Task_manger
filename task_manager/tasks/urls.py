from django.urls import path
from .views import CreateTaskView, UpdateTaskView, GetTaskView, DeleteTaskView

urlpatterns = [
    path('create', CreateTaskView.as_view(), name='create-task'),
    path('update', UpdateTaskView.as_view(), name='update-task'),
    path('get', GetTaskView.as_view(), name='get-task'),
    path('delete', DeleteTaskView.as_view(), name='delete-task'),
]
