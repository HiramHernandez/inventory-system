from django.db import models


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    id_cliente = models.IntegerField()
    id_vendedor = models.IntegerField()
    productos = models.TextField()
    impuesto = models.FloatField()
    neto = models.FloatField()
    total = models.FloatField()
    metodo_pago = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ventas'
