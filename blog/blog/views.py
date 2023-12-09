from django.http import HttpResponse

#render
from django.shortcuts import render

def contacto(request):
    return render(request, 'contacto.html')

def acerca_de(request):
    return render(request, 'acerca_de.html')

def categorias(request):
    return render(request, 'posts\categorias.html')