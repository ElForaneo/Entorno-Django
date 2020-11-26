from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Publicacione, Autor
from .forms import Publicacionesform

# Create your views here.

#def homePageView(request):
   # return render(request, 'Homepage.html', {})

class home(View):
    def get(self, request):

        publicaciones = Publicacione.objects.all()

        for pub in publicaciones:
            print(pub)

        context = {'publicaciones': publicaciones}
        return render(request, 'Homepage.html', context)

class Publicacionesadd(View):
    def get(self, request):
        form = Publicacionesform()
        context = {'form':form}
        return render(request, 'Publicaciones.html', context)

    def post(self, request):
        form = Publicacionesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = Publicacionesform()
            context = {'form':form}
            return render(request, 'Publicaciones.html', context)

class PublicacionesUpdate(View):
    def get(self, request,id):
        publicacion = Publicacione.objects.get(id=id)
        form = Publicacionesform(instance = publicacion)
        context = {'form':form}
        return render(request, 'Publicaciones.html', context)

    def post(self, request, id):
        publicacion = Publicacione.objects.get(id=id) 
        form = Publicacionesform(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = Publicacionesform()
            context = {'form':form}
            return render(request, 'Publicaciones.html', context)