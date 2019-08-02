from django.urls import path

from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    path('info/create/', views.info_create, name='info_create')
]