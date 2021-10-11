from django.http import HttpResponse
from django.shortcuts import render


def order(request):
    return HttpResponse('Hello! This is order application')
