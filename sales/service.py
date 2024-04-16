from django.db.models import Sum
from .models import Sale


class SaleService:
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def get_total(self):
        return Sale.objects.aggregate(total=Sum('neto'))['total']