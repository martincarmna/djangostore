from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index ,name='index'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_new, name='category_new'),
    path('categories/<int:cat_id>/', views.category_detail, name='category_detail'),
    path('categories/<int:cat_id>/update/', views.category_update, name='category_update'),
    path('categories/<int:cat_id>/delete/', views.category_delete, name='category_delete'),
    
    ]