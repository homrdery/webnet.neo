from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def index(request):
    messages.add_message(request, messages.INFO, "Hello world.")
    return render(request, 'index/page.html')

