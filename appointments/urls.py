from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('create/', views.appointment_create, name='appointment_create'),
    path('update/<int:id>/', views.appointment_update, name='appointment_update'),
    path('delete/<int:id>/', views.appointment_delete, name='appointment_delete'),
]
