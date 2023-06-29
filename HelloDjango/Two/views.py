from django.http import HttpResponse
from django.shortcuts import render


def helltwo(request):
    return HttpResponse("Hello Two")
