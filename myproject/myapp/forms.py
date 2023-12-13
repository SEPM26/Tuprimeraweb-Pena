from django import forms
from .models import Product, Customer


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
        

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)
