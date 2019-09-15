from django import forms
from django.db import transaction

from fcuser.models import Fcuser
from product.models import Product
from .models import Order


class OrderForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request


    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요'
        },
        label="수량"
    )

    product = forms.IntegerField(
        error_messages={
            'required': '상품을 선택해주세요'
        },
        widget=forms.HiddenInput, label="상품"
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        fcuser = self.request.session.get('user', None)

        if quantity and product and fcuser:

            with transaction.atomic():
                prod = Product.objects.get(pk=product)
                order = Order(quantity=quantity,
                              product=prod,
                              fcuser=Fcuser.objects.get(email=fcuser)
                              )
                order.save()

                prod.stock -= quantity
                prod.save()
        else:
            self.add_error("quantity", "값이 업습니다")
            self.add_error("product", "값이 업습니다")





