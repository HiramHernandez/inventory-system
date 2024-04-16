from django.db.models import Sum
from .models import Sale


class SaleService:
    
    __instance = None

    def __init__(self):
        if SaleService.__instance is not None:
            pass
            #raise Exception("Ya existe una instancia de CategoriaService")
        SaleService.__instance = self

    def get_total(self):
        return Sale.objects.aggregate(total=Sum('neto'))['total']