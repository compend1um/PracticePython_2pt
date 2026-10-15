from django.http import HttpResponseRedirect
from django.shortcuts import render


def redirect_to_navigator(_):
    return HttpResponseRedirect("/navigator")

def navigator(request):
    return render(request, "navigator.html")

def graphic_cards(request):
    return render(request, "graphic_cards.html")

def cases(request):
    return render(request, "cases.html")

def hdd(request):
    return render(request, "hdd.html")

def motherboards(request):
    return render(request, "motherboards.html")

def power_supply(request):
    return render(request, "power_supply.html")

def processors(request):
    return render(request, "processors.html")

def ram(request):
    return render(request, "ram.html")

def ssd(request):
    return render(request, "ssd.html")










