"""globalpowertools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myshop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('user_login/', views.user_login,name='user_login'),
    path('profile/', views.profile,name='profile'),
    path('admin_login/', views.admin_login,name='admin_login'),
    path('admin_profile/', views.admin_profile,name='admin_profile'),
    path('user_delete/<int:id>',views.user_delete,name='user_delete'),

    path('user_logout/', views.user_logout,name='user_logout'),


]
