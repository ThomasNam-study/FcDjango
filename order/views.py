from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView

from order.forms import OrderForm


class OrderCreate(FormView):
    form_class = OrderForm
    success_url = "/product/"

    def form_invalid(self, form):
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()

        kw.update({
            'request': self.request
        })

        return kw

