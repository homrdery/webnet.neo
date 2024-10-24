from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout  import Submit, Button, Reset
from crispy_forms.bootstrap import FormActions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", required=True)
    password = forms.CharField(label="Пароль", required=True, widget=forms.PasswordInput)
    next = forms.CharField(widget=forms.HiddenInput(), initial="/")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

class RegForm(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn-danger',  formnovalidate='formnovalidate',))
        self.helper.add_input(Reset('reset', 'Reset'))
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    def save (self, commit=True):
        user = super(RegForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
