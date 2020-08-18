"""proyectoDog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from appPerritos import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('mascotas', views.mascotas, name="mascotas"),
    path('busqueda_mascota/', views.busqueda_mascota),
    path('buscar/', views.buscar),
    path('mascota-list/',views.mascota_list, name="mascota_listar"),
    path('create/', views.create, name='create'),
    path('add_perrito/', views.add_perrito, name='add_perrito'),
    path('edit/<id>', views.edit ),
    path('update/<id>/', views.update, name='update' ),
    path('delete/<id>/', views.delete, name='delete' ),
]
