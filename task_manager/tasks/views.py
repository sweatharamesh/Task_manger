from rest_framework.views import APIView
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

class CreateTaskView(APIView):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        serializer = TaskSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('get-task')
        return render(request, "index.html", {"errors": serializer.errors})


class UpdateTaskView(APIView):
    def get(self, request):
        task_id = request.GET.get("id")
        task = Task.objects.get(id=task_id)
        print(task)
        return render(request, "update.html", {"data": task})

    def post(self, request):
        task_id = request.POST.get("id")
        task = Task.objects.get(id=task_id)
        title = request.POST.get("title")
        owner = request.POST.get("owner")
       

        if title and owner:
            task.title = title
            task.owner = owner
            task.save()
            return redirect("get-task")

        return render(request, "update.html", {"task": task, "error": "Title and Owner are required"})


class GetTaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return render(request, "view.html", {"data": serializer.data})

class DeleteTaskView(APIView):
    def post(self, request):
        task_id = request.POST.get('id')
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return redirect('get-task')
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
