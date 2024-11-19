from django.contrib import admin
from django.urls import path, include # type: ignore
from django.contrib.auth import views as auth_views
from user import views as user_views

urlpatterns = [
    path('',user_views.home, name='home'), 
    path('admin/', admin.site.urls),
    path('appointments/', include('appointments.urls')),  
    path('doctors/', include('doctors.urls')),  
    path('patients/', include('patients.urls')), 
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('register/', user_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]
