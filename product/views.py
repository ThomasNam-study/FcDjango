from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, FormView

from product.forms import RegisterForm
from product.models import Product


class ProductList(ListView):
    model = Product
    template_name = "product.html"
    context_object_name = "product_list"


class ProductCreate(FormView):
    template_name = "regist_product.html"
    form_class = RegisterForm
    success_url = "/product/"