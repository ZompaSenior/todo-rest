from django.urls import path

from . import views

urlpatterns = [
    path('newtask/', views.NewTaskView.as_view(), name = 'newtask'),
    path('edittask/', views.EditTaskView.as_view(), name = 'edittask'),
    path('deletetask/', views.DeleteTaskView.as_view(), name = 'deletetask'),
    path('tasklist/', views.TaskListView.as_view(), name = 'tasklist'),
]