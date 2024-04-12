from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria auto-incrementable
    categoria = models.TextField(max_length=255)  # Campo de texto con longitud máxima
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora con actualización automática

    class Meta:
        db_table = 'categorias'  # Nombre de la tabla en la base de datos
        verbose_name = 'Categoría'  # Nombre singular del modelo en el admin de Django
        verbose_name_plural = 'Categorías'  # Nombre plural del modelo en el admin de Django
