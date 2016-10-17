from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from models import BookAppointmentForm, ContactMeForm


def book(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        second_name=request.POST['second_name']
        gender=request.POST['gender']
        email_address=request.POST['email_address']
        phone_number=request.POST['phone_number']
        date=request.POST['date']
        source=request.POST['source']
        specification_source=request.POST['specification_source']

        BookAppointments.objects.create(
            first_name=first_name,
            second_name=second_name,
            gender=gender,
            email_address=email_address,
            phone_number=phone_number,
            date=date,
            source=source,
            specification_source=specification_source)
        return HttpResponse()
    else:
        return render(request, '/home.html/#Book')

def home(request):
    return render(request, 'home.html')

def former(request):
    return render(request, 'index.html')

def forms(request):
    if request.POST:
        form=BookAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/forms/')
    else:
        form=BookAppointmentForm()
        return render(request, 'forms.html',{'form':form})
