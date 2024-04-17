from django.urls import path
from .views import show_dashboard, ventas_por_dia


urlpatterns = [
    path('', show_dashboard, name='dashboard'),
    path('ventas-por-dia', ventas_por_dia, name='ventas-por-dia'),
]