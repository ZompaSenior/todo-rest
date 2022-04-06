from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.NewView.as_view(), name='new'),
    path('del/', views.DelView.as_view(), name='del'),
    path('psw/', views.PswView.as_view(), name='psw'),
]