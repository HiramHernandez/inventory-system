from datetime import date, timedelta


def str_to_date(date_str):
    return date_str.strftime("%Y-%m-%d")

def transform_venta_por_dia(venta_por_dia):
    new_venta = venta_por_dia.copy()
    new_venta['fecha__date'] = str(venta_por_dia['fecha__date'])
    return new_venta