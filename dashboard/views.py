from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.
def Dashboard(request):
    return render(request, 'dashboard.html')