#! coding: utf-8

from django.shortcuts import render

# Create your views here.
def welcome_page(request):
    return render(request, 'index.html', locals())
