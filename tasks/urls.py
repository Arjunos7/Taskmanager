from django.urls import path
from .views import UserTaskList, TaskUpdateView, TaskReportView

urlpatterns = [
    path('tasks/', UserTaskList.as_view(), name='user-tasks'),
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='update-task'),
    path('tasks/<int:pk>/report/', TaskReportView.as_view(), name='task-report'),
]
