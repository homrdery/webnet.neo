from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index/page.html')

