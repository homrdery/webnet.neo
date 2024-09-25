from django import forms
from crispy_forms.helper import FormHelper, Submit


class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", required=True)
    password = forms.CharField(label="Пароль", required=True)
    next = forms.CharField(widget=forms.HiddenInput(), initial="/")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

