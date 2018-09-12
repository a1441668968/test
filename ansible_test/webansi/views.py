from django.shortcuts import render, HttpResponse


# Create your views here.
def mainpage(request):
    return HttpResponse('mainpage')


def index(request):
    return HttpResponse('index')


def addhosts(request):
    return HttpResponse('addhosts')


def addmodules(request):
    return HttpResponse('addmodules')


def tasks(request):
    return HttpResponse('tasks')
