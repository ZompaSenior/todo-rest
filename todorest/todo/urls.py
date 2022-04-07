from django.urls import path

from . import views

urlpatterns = [
    path('newtask/', views.NewTaskView.as_view(), name = 'newtask'),
]