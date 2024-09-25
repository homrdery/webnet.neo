from django import forms
from crispy_forms.helper import FormHelper


class LoginForm(forms.Form):
    username = forms.CharField("Логин")
    password = forms.CharField("Пароль")
    next = forms.CharField("Логин")

   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'


