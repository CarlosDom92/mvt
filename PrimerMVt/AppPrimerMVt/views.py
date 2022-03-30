from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppPrimerMVt.models import * 
from AppPrimerMVt.forms import *


# Create your views here.
def familiares(request):
    if request.method == 'POST':
        miFormulario = FamiliaresFormulario(request.POST) #aquí mellega toda la información del html
        print(miFormulario)
        if miFormulario.is_valid:   #Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            familiar = Familiares(nombre=informacion['nombre'], apellidos=informacion['apellidos'], fechaNacimiento=informacion['fechaNacimiento']) 
            familiar.save()
            integrantes = Familiares.objects.all() #trae todos los profesores
            contexto= {"familiares":integrantes} 
            return render(request, "AppPrimerMVt/inicio.html",contexto) #Vuelvo al inicio o a donde quieran
    else:
        miFormulario= FamiliaresFormulario() #Formulario vacio para construir el html
    return render(request, "AppPrimerMVt/familiares.html", {"miFormulario":miFormulario})

def inicio(request):
    familiares = Familiares.objects.all() #trae todos los profesores
    contexto= {"familiares":familiares} 
    return render(request, "AppPrimerMVt/inicio.html",contexto)