from django.http import HttpResponseRedirect
from django.shortcuts import render
import os.path

def get_content_list():
    cat = []
    dirpath = os.path.dirname(os.path.abspath(__file__))
    # Чтение всех строк до конца файла
    f = open('D:\PracticePython_2pt\web_Hello_var_15\web_Hello_var_15\\tablica\hard_data.txt', "r", encoding="utf-8")
    for line in f:  # Построчное чтение до конца файла
        cat.append(line)#print(line, end='')
    f.close()
    #cat = ["Ноутбуки", "Принтеры", "Сканеры", "Системные блоки", "Роутеры", "Диски"]
    return cat



def redirect_to_navigator(_):
    return HttpResponseRedirect("/navigator")

def redirect_to_homepage(_):
    return HttpResponseRedirect("/homepage")

def navigator(request):
    return render(request, "navigator.html")

def homepage(request):
    content_list = get_content_list()
    return render(request, 'home.html', context={'content_list':content_list})

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










