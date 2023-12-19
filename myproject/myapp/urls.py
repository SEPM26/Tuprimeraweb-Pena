from django.urls import path
from .views import product_create, customer_create, search
from .views import ListaCategoriasView


urlpatterns = [
    path('product/create/', product_create, name='product_create'),
    path('customer/create/', customer_create, name='customer_create'),
    path('search/', search, name='search'),
    path('categorias/', ListaCategoriasView.as_view(), name='lista_categorias'),

]

