from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>polls</h1>It is now %s.</body></html>" % now
    return HttpResponse(html)
