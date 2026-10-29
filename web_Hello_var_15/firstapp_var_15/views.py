from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import os.path
import pandas as pd
from . import forms

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

def client(request):
    userform = forms.UserForm()
    return render(request, "client.html",{"form":userform})

def postuser(request):
    name = request.POST.get("name", "Undefined")
    surname = request.POST.get("surname", "Undefined")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {surname}</h2>")

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


# Функция для показа формы и приема данных
def buy_component(request):
    if request.method == 'POST':
        form = forms.PurchaseForm(request.POST)
        if form.is_valid():
            # Берем данные из формы
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            component = form.cleaned_data['component']
            # Склеиваем галочки через запятую (например, "Гарантия, Доставка")
            extras = ", ".join(form.cleaned_data['extras'])

            if not extras:
                extras = "Нет"

            # Записываем в Excel
            file_path = os.path.join(settings.BASE_DIR, "web_Hello_var_15", "tablica", "purchase_log.xlsx")

            # Создаем строчку для таблицы
            new_row = pd.DataFrame([{
                'Имя': name,
                'Комплектующее': component,
                'Количество': quantity,
                'Дополнительно': extras
            }])

            # Если файл есть - дописываем, если нет - создаем
            if os.path.exists(file_path):
                old_data = pd.read_excel(file_path)
                pd.concat([old_data, new_row]).to_excel(file_path, index=False)
            else:
                new_row.to_excel(file_path, index=False)

            # ПЕРЕАДРЕСАЦИЯ (GET-запрос) на страницу результата
            # Мы просто добавляем данные в конец адресной строки
            return redirect(f'/success/?name={name}&comp={component}&qty={quantity}&extras={extras}')
    else:
        form = forms.PurchaseForm()

    return render(request, "buy.html", {'form': form})


# Функция для страницы результата (принимает GET-запрос)
def purchase_success(request):
    # Достаем данные из адресной строки
    context = {
        'name': request.GET.get('name'),
        'comp': request.GET.get('comp'),
        'qty': request.GET.get('qty'),
        'extras': request.GET.get('extras'),
    }
    return render(request, "purchase_result.html", context)









