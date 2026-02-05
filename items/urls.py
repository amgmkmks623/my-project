from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # 商品
    path('add/', views.add_item, name='add_item'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
    path('toggle/<int:item_id>/', views.toggle, name='toggle'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),

    # カテゴリ
    path('category/add/', views.add_category, name='add_category'),
    path('category/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('category/edit/<int:category_id>/', views.edit_category, name='edit_category'),
]