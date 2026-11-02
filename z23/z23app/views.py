
from django.shortcuts import render
from datetime import date
from datetime import time
from .models import GPU, Customer, Enrollment
from django.http import HttpResponseRedirect

# получение данных из бд
def index(request):
    # фильтрация
    customers = Customer.objects.all()
    return render(request, "index.html", {"customers": customers})

def create(request):
    initialize()
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        customer = Customer()
        customer.name = request.POST.get("name")
        customer_ids = request.POST.getlist("gpus")
        customer.save()
        # получаем все выбранные курсы по их id
        gpus = GPU.objects.filter(id__in=customer_ids)
        customer.courses.set(gpus, through_defaults={"date": date.today(), "price": 0})
        return HttpResponseRedirect("/")

    gpus = GPU.objects.all()
    return render(request, "create.html", {"gpus": gpus})

def initialize():
    if GPU.objects.all().count() == 0:
        GPU.objects.create(name="RTX 4060")
        GPU.objects.create(name="RTX 2060 SUPER")
        GPU.objects.create(name="RTX 3070")
        GPU.objects.create(name="RTX 5080")


