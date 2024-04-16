from django.db.models import Count
from .models import Cliente

class ClienteService:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    
    def total_clientes(self):
        return Cliente.objects.aggregate(total=Count('id'))['total']
