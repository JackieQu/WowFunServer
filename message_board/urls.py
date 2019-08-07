from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('msg/', views.msg, name='msg'),
    path('msg/create/', views.msg_create, name='msg_create'),
]