from django.db.models import Count
from .models import Product


class ProductService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def get_total(self):
        return Product.objects.aggregate(total=Count('id'))['total'] 