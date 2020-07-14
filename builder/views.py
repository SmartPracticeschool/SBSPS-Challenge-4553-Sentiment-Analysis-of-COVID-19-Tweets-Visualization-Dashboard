from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.

def blank(request):
    return render(request,'blank.html')

def contact(request):
    return render(request,'contact.html')

def crowd_pred(request):
    return render(request,'crowd-pred.html')

def crowd_prediction(request):
    return render(request,'crowd-prediction.html')

def fake_info(request):
    return render(request,'fake-info.html')

def fake_info_prediction(request):
    return render(request,'fake-info-prediction.html')

def general(request):
    return render(request,'general.html')

def index(request):
    return render(request,'index.html')

def location_analysis(request):
    return render(request,'location-analysis.html')

def login(request):
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')

def thank_you(request):
    return render(request,'thank-you.html')

def widgets(request):
    return render(request,'widgets.html')


