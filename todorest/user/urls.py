from django.urls import path

from . import views

urlpatterns = [
    path('subscribe/', views.SubscribeView.as_view(), name = 'subscribe'),
    path('unsubscribe/', views.UnsubscribeView.as_view(), name = 'unsubscribe'),
    path('changepassword/', views.ChangePasswordView.as_view(), name = 'changepassword'),
]