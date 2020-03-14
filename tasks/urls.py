from django.urls import path
from . import views

urlpatterns = [
    path('',views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='task-new'),
    path('edit/<int:id>',views.editTask,name='task-edit'),
    path('delete/<int:id>',views.deleteTask,name='task-dele')
]