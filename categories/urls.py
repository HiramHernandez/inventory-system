from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_categories, name='list_categories'),
    path('save-category', views.save_category, name='save-category'),
    path('edit-category/<int:id>/', views.edit_category, name='edit-category'),
    path('remove-category/<int:id>/', views.remove_category, name='remove-category'),
]