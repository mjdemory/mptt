from django.shortcuts import render, HttpResponseRedirect
from dropbox_mini.models import Boxofdrop



# Create your views here.

def index (request):
    html = "index.html"
    tree = Boxofdrop.objects.all()
    return render(request, html, {'post': tree})