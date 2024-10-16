from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import dirAddr
from .forms import addFormAddr
import logging
# from .forms import delFormAddr, reFormAddr,
APPNAME = "client"
logger = logging.getLogger(APPNAME)
# Create your views here.

def adr(request):
    return render(request, "directory/addr.html")


def addr(request):
    error = ""
    if request.method == "POST":
        action = request.POST.get("action")
        # if action == "delAddr":
        #     id = int(request.POST.get("id"))
        #     try:
        #         obj = dirAddr.objects.get(id=id)
        #         obj.delete()
        #     except dirAddr.DoesNotExist as e:
        #         logger.error(f"Не существует {id}")
        # if action == "reAddr":
        #     try:
        #
        #         id = int(request.POST.get("id"))
        #         obj = dirAddr.objects.get(id=id)
        #         form = reFormAddr(request.POST, instance=obj)
        #         if form.is_valid():
        #             form.save()
        #         else:
        #             error = form.errors
        #             logger.error(error)
        #     except dirAddr.DoesNotExist as e:
        #         logger.error(f"Не существует {id}")
        if action == "subAddr":
            form = addFormAddr(request.POST)
            if form.is_valid():
                form.save()
            else:
                error = form.errors
    names = dirAddr.objects.all().order_by("id")
    params = {
        "names": names,
        "eror": error,
        "title": f"всего компов"
    }
    return render(request, "directory/dirAddr.html", params)


def getform(request):
    if request.method == 'GET':
        action = request.GET.get("action")
        if action == "subAddr":
            form = addFormAddr()
        if action == "delAddr":
            id = request.GET.get("id", False)
        #     if id:
        #         obj = dirAddr.objects.get(id=id)
        #         form = delFormAddr(instance=obj)
        # if action == "reAddr":
        #     id = request.GET.get("id", False)
        #     # name = request.GET.get('name', False)
        #     if id:
        #         obj = dirAddr.objects.get(id=id)
        #         form = reFormAddr(instance=obj)

    params = {
        "form": form,
    }
    return render(request, "directory/ForForms/addForm.html", params)

# Create your views here.
