from django.shortcuts import render

# Create your views here.
def dir_pktread():
    return render(request, "DirPktreader/DirPktreader.html")