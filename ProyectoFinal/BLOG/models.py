from django.db import models


class Autor(models.Model):

    class Meta:
        verbose_name_plural="Autores"

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)


class Articulo(models.Model):

    class Meta:
        verbose_name_plural="Articulos"

    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null=True)


class Seccion(models.Model):

    class Meta:
        verbose_name_plural="Secciones"

    nombre = models.CharField(max_length=100)
