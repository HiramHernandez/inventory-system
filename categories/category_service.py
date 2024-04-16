from django.db.models import Count
from .models import Category

class CategoryService:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    # retonar success, objeto
    def crear_categoria(self, nombre):
        try:
            categoria = Category(categoria=nombre)
            categoria.save()
            return (True, categoria)
        except Exception:
            return (False, None)

    def fetch(self):
        try:
            return Category.objects.all()
        except Category.DoesNotExist:
            return None

    def obtener_categoria(self, id):
        try:
            return Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return None

    def actualizar_categoria(self, id, nombre):
        try:
            categoria = Category.objects.get(pk=id)
            categoria.categoria = nombre
            categoria.save()
            return (True, categoria)
        except Exception:
            return (False, None)

    def eliminar_categoria(self, id):
        try:
            categoria = Category.objects.get(pk=id)
            categoria.delete()
            return True
        except Category.DoesNotExist:
            return False
        
    def total_categories(self):
        return Category.objects.aggregate(total=Count('id'))['total']

