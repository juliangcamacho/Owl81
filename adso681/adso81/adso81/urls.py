"""
URL configuration for adso81 project.

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
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('inventarios/', views.inventarios, name='inventarios'),
    path ('interfazcentral/',views.ic, name='interfazcentral'),
    path('blog/', views.blog, name='blog'),
    path('donaciones/', views.donaciones, name='donaciones'),
    path('login/', views.login, name='login'),
    path('novedades/', views.novedades, name='novedades'),
    path('regis_donacion/', views.regis_donacion, name='regis_donacion'),
    path('regis_novedad/',views.regis_novedad, name='regis_novedad'),
]
