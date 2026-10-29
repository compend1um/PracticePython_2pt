from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
import os.path
import pandas as pd

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
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "web_Hello_var_15", "tablica", "gpu.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict('records')
    context = {
        'headers': headers,
        'data': data,
        'title': 'GPU'
    }
    return render(request, "graphic_cards.html", context)

def cases(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "web_Hello_var_15", "tablica", "case.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict('records')
    context = {
        'headers': headers,
        'data': data,
        'title': 'Корпуса'
    }
    return render(request, "cases.html", context)

def hdd(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "web_Hello_var_15", "tablica", "hdd.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict('records')
    context = {
        'headers': headers,
        'data': data,
    }
    return render(request, "hdd.html", context)

def motherboards(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "web_Hello_var_15", "tablica", "motherboard.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict('records')
    context = {
        'headers': headers,
        'data': data,
    }
    return render(request, "motherboards.html", context)

def power_supply(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "web_Hello_var_15", "tablica", "power_supply.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict('records')
    context = {
        'headers': headers,
        'data': data,
    }
    return render(request, "power_supply.html", context)

def processors(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "web_Hello_var_15", "tablica", "cpu.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict('records')
    context = {
        'headers': headers,
        'data': data,
    }
    return render(request, "processors.html", context)

def ram(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "web_Hello_var_15", "tablica", "ram.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict('records')
    context = {
        'headers': headers,
        'data': data,
    }
    return render(request, "ram.html", context)

def ssd(request):
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "web_Hello_var_15", "tablica", "ssd.xlsx"))
    headers = df.columns.tolist()
    data = df.to_dict('records')
    context = {
        'headers': headers,
        'data': data,
    }
    return render(request, "ssd.html", context)










