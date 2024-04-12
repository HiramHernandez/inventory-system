from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_categories, name='list_categories'),
    path('edit-category/<int:id>/', views.edit_category, name='edit-category'),
]