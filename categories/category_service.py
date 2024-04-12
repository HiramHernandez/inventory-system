from django.db import models
from .models import Category

class CategoryService:

    __instance = None

    def __init__(self):
        if CategoryService.__instance is not None:
            pass
            #raise Exception("Ya existe una instancia de CategoriaService")
        CategoryService.__instance = self

    @staticmethod
    def get_instance():
        if CategoryService.__instance is None:
            CategoryService.__instance = CategoryService()
        return CategoryService.__instance

    def crear_categoria(self, nombre):
        categoria = Category(categoria=nombre)
        categoria.save()
        return categoria

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
            return categoria
        except Category.DoesNotExist:
            return None

    def eliminar_categoria(self, id):
        try:
            categoria = Category.objects.get(pk=id)
            categoria.delete()
            return True
        except Category.DoesNotExist:
            return False
