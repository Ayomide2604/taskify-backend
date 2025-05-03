from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-is_completed', 'created_at',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
