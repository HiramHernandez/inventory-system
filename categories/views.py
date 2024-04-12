from django.http import HttpResponse
from django.shortcuts import render
from .category_service import CategoryService

def list_categories(request):
    category_service = CategoryService()
    categories = category_service.fetch()
    context = {'categories': categories}
    return render(request, 'categories/index.html', context)


def edit_category(request, id):
    category_service = CategoryService()
    categories = category_service.fetch()
    context = {'categories': categories}
    return render(request, 'categories/index.html', context)