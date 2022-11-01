"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from usuario import views #importo desde django views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'), # desde aca cambio el index
    path('registrarse/', views.Logueo, name='logueo'),
    path('ingreso/', views.Ingreso, name='ingreso'),
    path('ingreso/tareas/', views.Tareas_Ingreso, name='Tareas_Ingreso'),
    path('ingreso/<int:notas_id>/', views.notas, name='notas'),
    path('salir/', views.Salir, name='salir'),
    path('signin/', views.Signin, name='signin'),
    
    
   
]
