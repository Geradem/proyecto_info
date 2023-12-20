from django.shortcuts import render, redirect
from django.urls import reverse


#usamos el registro que creamos nosotros
from .forms import FormularioRegistro

# importamos menssages para enviar un aviso

from django.contrib import messages
def registro(request):
    contexto = {}

    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            nombre_usuario = formulario.cleaned_data["username"]
            messages.success(request, f"El usuario {nombre_usuario} fue creado!!!")
            return redirect(reverse("posts:post_realizado"))
    else:
        formulario = FormularioRegistro()

    contexto["form"] = formulario
    return render(request, "usuarios/registro.html", contexto)