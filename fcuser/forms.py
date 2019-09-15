from django import forms
from django.contrib.auth.hashers import check_password, make_password

from fcuser.models import Fcuser

class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요'
        },
        max_length=64, label="이메일"
    )

    password = forms.CharField(
        error_messages={
            'required': '패스워드를 입력해주세요'
        },
        widget=forms.PasswordInput, label="비밀번호"
    )

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(email=username)
            except Fcuser.DoesNotExist:
                self.add_error("username", "존재하지 않는 아이디입니다")
                return

            if not check_password(password, fcuser.password):
                self.add_error("password", "비밀번호가 틀렸습니다")
            else:
                self.email = fcuser.email


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요'
        },
        max_length=64, label="이메일"
    )

    password = forms.CharField(
        error_messages={
            'required': '패스워드를 입력해주세요'
        },
        widget=forms.PasswordInput, label="비밀번호"
    )

    re_password = forms.CharField(
        error_messages={
            'required': '패스워드를 입력해주세요'
        },
        widget=forms.PasswordInput, label="비밀번호 확인"
    )

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error("password", "비밀번호가 틀렸습니다")
                self.add_error("re_password", "비밀번호가 틀렸습니다")
            else:
                fcuser = Fcuser(email=email, password=make_password(password))
                fcuser.save()
