from django.db import models

class Cliente(models.Model):
    nombre = models.TextField()
    documento = models.IntegerField()
    email = models.EmailField()
    telefono = models.TextField()
    direccion = models.TextField()
    fecha_nacimiento = models.DateField()
    compras = models.IntegerField()
    ultima_compra = models.DateTimeField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clientes'  # Nombre de la tabla en la base de datos
        verbose_name = 'Clientes'  # Nombre singular del modelo en el admin de Django
        verbose_name_plural = 'Clientes'  # Nombre plural del modelo en el admin de Django
