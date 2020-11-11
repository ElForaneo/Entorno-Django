from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    #return HttpResponse('Hola, estas muerto :)')
    return render(request, 'Homepage.html')

def CommentsView(request):
    return render(request, 'comments.html')

def AboutView(request):
    return render(request, 'About.html')
