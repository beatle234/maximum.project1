from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Успешно")

def lesson4(request):
    return HttpResponse("Домашка по 4 занятию")
