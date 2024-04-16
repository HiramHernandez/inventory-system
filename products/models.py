from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    id_categoria = models.IntegerField()  # Foreign key to Categoria model (likely)
    codigo = models.CharField(max_length=255)  # Text limited to 255 characters
    descripcion = models.TextField()  # Unlimited text for description
    imagen = models.URLField()  # URL for the product image
    stock = models.IntegerField()  # Number of items in stock
    precio_compra = models.FloatField()  # Purchase price
    precio_venta = models.FloatField()  # Selling price
    ventas = models.IntegerField()  # Number of units sold
    fecha = models.DateTimeField(auto_now_add=True)  # Timestamp with auto-update on creation and update

    class Meta:
        db_table = 'productos'  # Explicit table name mapping (optional)