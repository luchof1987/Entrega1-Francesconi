# Generated by Django 4.1.1 on 2022-10-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Articulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100)),
                ("texto", models.CharField(max_length=1000)),
                ("fecha", models.DateField(null=True)),
            ],
            options={
                "verbose_name_plural": "Articulos",
            },
        ),
        migrations.CreateModel(
            name="Autor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("profesion", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Autores",
            },
        ),
        migrations.CreateModel(
            name="Seccion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Secciones",
            },
        ),
    ]
