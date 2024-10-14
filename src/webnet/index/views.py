from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from addr.models import dirAddr
from .forms import addForm, reFormAddr, delFormAddr
import logging
from addr.models import Pktreader

# from .forms import delFormAddr, reFormAddr,
APPNAME = "client"
logger = logging.getLogger(APPNAME)
# Create your views here.

# Create your views here.


def index(request):
    # from addr.models import PktRecordLog
    # PktRecordLog.objects.compute()
    items = Pktreader.objects.index_list()
    return render(request, 'index/page.html', {"items": items})


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
        if action == "sub":
            form = addForm(request.POST)
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
    return render(request, "tables/Addr.html", params)



def getform(request):
    if request.method == 'GET':
        action = request.GET.get("action")
        if action == "subAddr":
            form = addForm()
        if action == "delAddr":
            mac_addr = request.GET.get("mac_addr", False)
            if mac_addr:
                obj = Pktreader.objects.get(mac_addr=mac_addr)
                form = delFormAddr(instance=obj)

        if action == "reAddr":
            mac_addr = request.GET.get("mac_addr", False)
            # name = request.GET.get('name', False)
            if mac_addr:
                obj = Pktreader.objects.get(mac_addr=mac_addr)
                form = reFormAddr(instance=obj)


    params = {
        "form": form,
    }
    return render(request, "index/ForForms/addForm.html", params)

