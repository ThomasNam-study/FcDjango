from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView, DetailView

from fcuser.decorators import login_required, admin_required
from order.forms import OrderForm
from product.forms import RegisterForm
from product.models import Product


class ProductList(ListView):
    model = Product
    template_name = "product.html"
    context_object_name = "product_list"


@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = "regist_product.html"
    form_class = RegisterForm
    success_url = "/product/"


class ProductDetail(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = OrderForm(self.request)

        return context
