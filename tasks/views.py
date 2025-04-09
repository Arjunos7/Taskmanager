from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAdminOrSuperAdmin


class UserTaskList(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class TaskReportView(generics.RetrieveAPIView):
    queryset = Task.objects.filter(status='completed')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSuperAdmin]
