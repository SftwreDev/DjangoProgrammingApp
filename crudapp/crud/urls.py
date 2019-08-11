from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name = 'list'),
    path('list/<str:slug>/', views.detail, name='detail'),
    path('create-new/', views.create, name='create'),
]
