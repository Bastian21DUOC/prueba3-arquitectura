from django.http import request
from django.shortcuts import render

def home(request):
    return render(request,'prueba3/home.html')


def login(request):
    return render(request,'prueba3/login.html')


def reserva(request):
    return render(request,'prueba3/reserva.html')