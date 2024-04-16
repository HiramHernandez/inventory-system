from django.db.models import Count
from .models import Cliente

class ClienteService:

    __instance = None

    def __init__(self):
        if ClienteService.__instance is not None:
            pass
            #raise Exception("Ya existe una instancia de CategoriaService")
        ClienteService.__instance = self

    @staticmethod
    def get_instance():
        if ClienteService.__instance is None:
            ClienteService.__instance = ClienteService()
        return ClienteService.__instance

    
    def total_clientes(self):
        return Cliente.objects.aggregate(total=Count('id'))['total']
