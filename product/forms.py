from django import forms

from product.models import Product


class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '상품명을 입력해주세요'
        },
        max_length=64, label="상품명"
    )

    price = forms.IntegerField(
        error_messages={'required': '상품가격을 입력해주세요'},
        label="상품가격"
    )

    description = forms.CharField(
        error_messages={
            'required': '설명을 입력해주세요'
        },
        widget=forms.PasswordInput, label="설명"
    )

    stock = forms.IntegerField(
        error_messages={'required': '재고를 입력해주세요'},
        label="재고"
    )

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        stock = cleaned_data.get('stock')

        if not(name and price and description and stock):
            self.add_error("name", "값이 없습니다")
            self.add_error("price", "값이 없습니다")
            self.add_error("description", "값이 없습니다")
            self.add_error("stock", "값이 없습니다")
