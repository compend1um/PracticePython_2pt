from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Brand
from .models import Model

def index(request):
    models = Model.objects.all()
    return render(request, "index.html", {"models": models})


def create(request):
    create_brands()  # добавляем начальные данные для компаний
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        model = Model()
        model.name = request.POST.get("name")
        model.price = request.POST.get("price")
        model.brand_id = request.POST.get("brand_id")
        model.save()
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    brands = Brand.objects.all()
    return render(request, "create.html", {"brands": brands})

def edit(request, id):
    try:
        model = Model.objects.get(id=id)

        if request.method == "POST":
            model.name = request.POST.get("name")
            model.price = request.POST.get("price")
            model.brand_id = request.POST.get("brand_id")
            model.save()
            return HttpResponseRedirect("/") # переход на index
        else:
            brands = Brand.objects.all()
            return render(request, "edit.html", {"model": model, "brands": brands})
    except Model.DoesNotExist:
        return HttpResponseNotFound("<h2>Model not found</h2>")


def delete(request, id):
    try:
        model = Model.objects.get(id=id)
        model.delete()
        return HttpResponseRedirect("/")
    except Model.DoesNotExist:
        return HttpResponseNotFound("<h2>Model not found</h2>")

# добавление начальных данных в таблицу компаний
def create_brands():
    if Brand.objects.all().count() == 0:
        Brand.objects.create(name="Apple")
        Brand.objects.create(name="Asus")
        Brand.objects.create(name="MSI")