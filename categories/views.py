from django.http import HttpResponse
from django.shortcuts import render, redirect
from .category_service import CategoryService

def list_categories(request):
    category_service = CategoryService()
    categories = category_service.fetch()
    context = {'categories': categories}
    return render(request, 'categories/index.html', context)

def save_category(request):
    category_service = CategoryService()
    name = request.POST.get("nuevaCategoria")
    success, _ = category_service.crear_categoria(name)
    if not success:
        return redirect('list_categories')
    return redirect('list_categories')
    
def edit_category(request, id):
    category_service = CategoryService()
    name = request.POST.get("editarCategoria")
    succes, _ = category_service.actualizar_categoria(id, name)
    if not succes:
        return redirect('list_categories')
    return redirect('list_categories')

def remove_category(request, id):
    category_service = CategoryService()
    success = category_service.eliminar_categoria(id)
    if not success:
        return redirect('list_categories')
    return redirect('list_categories')