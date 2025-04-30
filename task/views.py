from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer
# Create your views here.


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.order_by('created_at').all()
    serializer_class = TaskSerializer
