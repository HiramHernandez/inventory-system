import locale
import json
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from sales.service import SaleService
from categories.category_service import CategoryService
from clients.service import  ClienteService
from products.service import ProductService
# Create your views here.

def show_dashboard(request):
    sale_service = SaleService()
    sale_total = sale_service.get_total()

    category_serivice = CategoryService()
    cliente_service = ClienteService()
    product_service = ProductService()

    fecha_inicial = None #date(2024, 4, 1)  # Reemplaza con la fecha deseada
    fecha_final = date(2024, 4, 15)  # Reemplaza con la fecha deseada

    ventas = sale_service.obtener_ventas(fecha_inicial, fecha_final)
    

        

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    context={
        'total_ventas': sale_total,
        'total_categorias': category_serivice.total_categories(),
        'total_clientes': cliente_service.total_clientes(),
        'total_productos': product_service.get_total()
    }

    return render(request, 'dashboard.html', context=context)


def ventas_por_dia(request):
    sale_service = SaleService()
    json_data = json.dumps(sale_service.total_ventas_por_dia())
    return HttpResponse(json_data, content_type='application/json')
    