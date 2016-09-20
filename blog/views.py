from django.shortcuts import render

# Create your views here.
def home(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>blog</h1>It is now %s.</body></html>" % now
    return HttpResponse(html)
