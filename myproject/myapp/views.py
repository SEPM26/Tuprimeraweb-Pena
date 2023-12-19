from django.shortcuts import render, redirect
from .models import Product, Customer, Categoria
from .forms import ProductForm, CustomerForm, SearchForm, CategoriaForm
from django.views.generic.base import View



def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_create')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_create')
    else:
        form = CustomerForm()
    return render(request, 'customer_create.html', {'form': form})

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            products = Product.objects.filter(name__icontains=search_query)
            return render(request, 'search_results.html', {'products': products})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

class ListaCategoriasView(View):
    template_name = 'lista_categorias.html'

    def get(self, request):
        categorias = Categoria.objects.all()
        form = CategoriaForm()
        return render(request, self.template_name, {'categorias': categorias, 'form': form})

    def post(self, request):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')

        categorias = Categoria.objects.all()
        return render(request, self.template_name, {'categorias': categorias, 'form': form})
