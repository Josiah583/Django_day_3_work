from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products, name ='products'),
    path('products/<int:id>', views.product, name ='products'),
    path('store', views.stores, name ='store'),
    path('store/<int:id>', views.stores, name ='store'),
    path('store/<int:id>/products', views.stores_products, name ='store_products'),
    path('categories', views.categories, name ='category'),
    path('categories/<int:id>', views.categories, name ='category'),


]