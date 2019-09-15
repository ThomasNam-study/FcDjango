from django.db import transaction
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import FormView, ListView

from fcuser.decorators import login_required
from fcuser.models import Fcuser
from order.forms import OrderForm
from order.models import Order
from product.models import Product


@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = OrderForm
    success_url = "/product/"

    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(quantity=form.data.get('quantity'),
                          product=prod,
                          fcuser=Fcuser.objects.get(email=self.request.session.get('user'))
                          )
            order.save()

            prod.stock -= int(form.data.get('quantity'))
            prod.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()

        kw.update({
            'request': self.request
        })

        return kw


@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = "order.html"
    context_object_name = "order_list"

    def get_queryset(self):
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))

        return queryset


