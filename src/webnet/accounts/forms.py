from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout  import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", required=True)
    password = forms.CharField(label="Пароль", required=True)
    next = forms.CharField(widget=forms.HiddenInput(), initial="/")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

# class RegForm(UserCreationForm):
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         Fields = ("username", "email", "password1", "password2")
    # def save (self, commit=True):
    #     user = super(RegForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user