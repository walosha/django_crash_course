from django.shortcuts import render
from django.http import HttpResponse
from .choices import  bedroom_choices,state_choices,price_choices


def index(request):
    context =  { 
        "state_choices":state_choices,
    "bedroom_choices":bedroom_choices,
    "price_choices":price_choices
    }
    return render(request, 'pages/index.html',context)


def about(request):
    return render(request, 'pages/about.html', )
