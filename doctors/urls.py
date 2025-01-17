
from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),  
    path('create/', views.doctor_create, name='doctor_create'),  
    path('<int:id>/update/', views.doctor_update, name='doctor_update'),  
    path('<int:id>/delete/', views.doctor_delete, name='doctor_delete'), 
]
