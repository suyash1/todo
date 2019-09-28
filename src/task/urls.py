from django.urls import path

from . import views

urlpatterns = [
    path('task', views.TaskAPI.as_view(), name='task_api'),
    path('task/<str:task_id>', views.TaskAPI.as_view(), name='get_task_by_id'),
]
