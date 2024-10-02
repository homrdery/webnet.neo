from django.shortcuts import render,redirect
from .forms import LoginForm, RegForm
from django.contrib import auth, messages
from django.contrib.auth import login
from .decarators import anonymous_required
# Create your views here.
@anonymous_required
def register(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            else:
                messages.add_message(request, messages.ERROR, f"Ошибка Логина введите вручную")
                redirect("accounts/login/")
            return redirect("/")

        else:
            messages.add_message(request, messages.ERROR, f"Ошибка создания пользователя")
    else:
        form = RegForm()
    return render(request, "accounts/reg.html", context={"form": form})
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
                messages.add_message(request, messages.ERROR, f"Ошибка аунтификации")
        else:
            messages.add_message(request, messages.ERROR, f"Ошибка пользователь не найден")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", context={"form": form})

def logout(request):
    auth.logout(request)
    return redirect("/")
