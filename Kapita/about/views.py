from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def AboutView(request):
    return render(request, 'About.html',{})
