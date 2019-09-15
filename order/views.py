from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import FormView, ListView

from fcuser.decorators import login_required
from order.forms import OrderForm
from order.models import Order

@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = "order.html"
    context_object_name = "order_list"

    def get_queryset(self):
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))

        return queryset


