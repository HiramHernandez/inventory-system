from django.db import models
from django.db.models import Sum, Q, Count
from django.db.models.expressions import Value, F, Case, When
from django.core.cache import cache
from .models import Sale
from utils.format import str_to_date, transform_venta_por_dia


class SaleService:
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def get_total(self):
        return Sale.objects.aggregate(total=Sum('neto'))['total']
    

    def obtener_ventas(self, fecha_inicial, fecha_final):
        #if fecha_inicial > fecha_final:
        #    raise ValueError("La fecha inicial debe ser menor o igual a la fecha final")

        ventas = []

        match fecha_inicial == None:
            case True:
                ventas = Sale.objects.all().order_by('-id')
            case False:
                date_filter = Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final)
                ventas =  Sale.objects.filter(date_filter).order_by('-id')
            case _:
                raise ValueError("Lo sentimos ocurrido un error inesperado")  
        return ventas
    
    def total_ventas_por_dia(self, avoid_cache):
        cache_key = 'total_ventas_por_dia'
        ventas_por_dia_cached = cache.get(cache_key)
        not_using_cache = ventas_por_dia_cached is None or avoid_cache
        if not_using_cache:
            ventas_por_dia = Sale.objects.values('fecha__date') \
                .annotate(ventas_por_dia=Count('id'), total_por_dia=Sum('total')) \
                .order_by('fecha__date') \
                .all()
            result_serializeds = [transform_venta_por_dia(venta) for venta in ventas_por_dia]
            cache.set(cache_key, result_serializeds, timeout=60 * 60)
            return result_serializeds

        return ventas_por_dia_cached
