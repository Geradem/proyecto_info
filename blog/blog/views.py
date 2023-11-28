from django.http import HttpResponse

#render
from django.shortcuts import render

def saludo(request):
    return render(request, 'index.html')

def despedida(request):
    return HttpResponse('buenas ncohes')

def nombre(request):
    return HttpResponse('daniel'+'frias')