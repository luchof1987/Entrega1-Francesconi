from django.contrib import admin
from django.urls import path, include
from BLOG.views import mostrar_inicio

urlpatterns = [
    path("inicio/", mostrar_inicio),
]
