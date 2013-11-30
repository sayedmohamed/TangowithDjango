from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('hello rango')


def about(request):
    return HttpResponse('rango says:good bye')
