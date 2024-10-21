from django.shortcuts import render

# Create your views here.
def logs(request):
    error = ""
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "sub":
            form = addForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                error = form.errors

    items = Pktreader.objects.all().order_by("time")
    names = worker.objects.all().order_by("id")

    params = {
        "names": names,
        "items": items,
        "error":error,

        "title": f"всего компов"
    }
    return render(request, "logs/logs.html", params)
