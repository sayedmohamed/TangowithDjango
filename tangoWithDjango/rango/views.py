from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext


def index(request):
	context=RequestContext(request)
	return render(request,'rango/index.html',context)


def about(request):
    return HttpResponse('rango says:good bye')
