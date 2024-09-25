from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib import auth


# Create your views here.

def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            next = form.cleaned_data.get('next')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(next)
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", context={"form": form})
