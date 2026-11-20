from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.drink_list, name='drink_list'),
    path('<int:pk>/', views.drink_detail, name='drink_detail'),
]