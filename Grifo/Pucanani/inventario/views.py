from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def new(request):
    return HttpResponse("A er???")

def inventario(request):
    return HttpResponse("ESTE ES EL INVENTARIO")