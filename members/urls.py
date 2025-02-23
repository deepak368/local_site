"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views
from .views import UserRegisterView

urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('login_user', views.login_user, name = 'login'),
    path('logout', views.logout_user, name = 'logout'),
    path('register_user', views.user_register, name = 'user_register'),
    path("register",UserRegisterView.as_view(),name="register"),

   
]
