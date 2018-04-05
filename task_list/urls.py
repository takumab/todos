from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.index, name='tasks'),
    path('tasks/<int:task_id>', views.delete_task, name='delete'),
    path('tasks/<int:task_id>/completed', views.completed, name="completed"),
    path('', views.welcome, name='welcome')
]