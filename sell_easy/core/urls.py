from django.urls import path, include
from . import views
from core.account import views as account_views 

urlpatterns = [
    path('products', views.products, name ='products'),
    path('products/<int:id>', views.product, name ='products'),
    path('store', views.stores, name ='store'),
    path('store/<int:id>', views.stores, name ='store'),
    path('store/<int:id>/products', views.stores_products, name ='store_products'),
    path('categories', views.categories, name ='category'),
    path('categories/<int:id>', views.categories, name ='category'),

]
    # ACCOUNT VIEES

path('account/', include([
    path('login', account_views.login, name='login'),
    path('signup', account_views.signup, name='sign-up'),

])),

path('dasboard', account_views.dasboard, name='dasboard'),