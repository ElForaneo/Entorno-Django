from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def commentsView(request):
    return render(request, 'comments.html',{})
