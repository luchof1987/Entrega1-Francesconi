from django.shortcuts import render
from django.http import HttpResponse


def mostrar_inicio(resquest):
    return HttpResponse("este es el inicio")
