from django.shortcuts import render, redirect
from .models import *
from .urls import *
from .forms import *

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
# Create your views here.

from django.http import HttpResponse


def inicio(request):

    context = {}
    direccion = "inicio.html"
    return render(request, direccion, context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------Manuscrito---------------------------------------- #
# ----------------------------------------------------------------------------------- #

def cargar_manuscrito(request):

    context = {}
    if request.method == 'POST':
        form = ManuscriptForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ManuscriptForm()
    
    titulo = "Manuscrito"
    context['form'] = form
    context['titulo'] = titulo
    direccion = "cargar.html"

    return render(request, direccion, context)

def listar_manuscritos(request):
    return

def mostrar_manuscrito(request):
    return

def modificar_manuscrito(request):
    return

def borrar_manuscrito(request):
    return



