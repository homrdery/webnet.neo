from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from addr.models import dirAddr, Pktreader
from .forms import addForm, reFormAddr, delFormAddr
import logging
from addr.models import Pktreader

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
        if action == "delAddr":
            mac_addr = str(request.POST.get("mac_addr"))
            try:
                obj = Pktreader.objects.get(mac_addr=mac_addr)
                obj.delete()
            except Pktreader.DoesNotExist as e:
                logger.error(f"Не существует {mac_addr}")
        if action == "reAddr":
            try:

                mac_addr = request.POST.get("mac_addr")
                obj = Pktreader.objects.get(mac_addr=mac_addr)
                form = reFormAddr(request.POST, instance=obj)
                if form.is_valid():
                    form.save()
                else:
                    error = form.errors
                    logger.error(error)
            except Pktreader.DoesNotExist as e:
                logger.error(f"Не существует {mac_addr}")
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

