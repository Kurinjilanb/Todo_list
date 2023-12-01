from .serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet
from TodoApp.models import Task

class TaskViewset(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer