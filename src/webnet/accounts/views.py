from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate


# Create your views here.

def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            next = form.cleaned_data.get('next')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(next)
        else:
            form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})
