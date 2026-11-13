from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Gpu
from .models import Customer
from .models import SpecGpu

def homepage(request):
    return render(request, "homepage.html")

def customers(request):
    clients = Customer.objects.all()
    return render(request, "customers.html", {"clients": clients})

def sales_progress(request):
    return render(request, "sales_progress.html")

def products(request):
    create_gpus_new()
    gpus = Gpu.objects.all()
    return render(request, "products.html", {"gpus": gpus})

def sale(request):
    return render(request, "sale.html")

def create_gpu(request):
    create_gpus_new()
    return render(request, "create_gpu.html")

def edit_customer(request, id):
    if request.method == "POST":
        customer = Customer.objects.get(id=id)
        customer.name = request.POST.get("customer")
        customer.save()
        return redirect("customers")
    return render(request, "edit_customer.html")

def edit_gpu(request, id):
    return render(request, "edit_gpu.html", context={"id":id})

def success_buy(request):
    return render(request, "success_buy.html")

def create_client(request):

    if request.method == "POST":
        customer = Customer()
        customer.name = request.POST.get('customer')
        customer.save()
        return redirect("customers")
    return redirect("customers")

def delete_customer(request, id):
    try:
        customer = Customer.objects.get(id=id)
        customer.delete()
        return redirect('customers')
    except Customer.DoesNotExist:
        return HttpResponseNotFound("<h2> Клиент не найден </h2>")

def delete_gpu(request, id):
    try:
        gpu = Gpu.objects.get(id=id)
        gpu.delete()
        return redirect('products') # Возвращаемся к списку
    except Customer.DoesNotExist:
        return HttpResponseNotFound("<h2> Gpu не найденa </h2>")

def create_gpus_new():
    if Gpu.objects.all().count() == 0:
        spec1 = SpecGpu.objects.create(frequency_Mhz=2280, type_memory_str="GDDR7", memory_size_Gb=8)
        Gpu.objects.create(name="Nvidia RTX 5060", price=50000, spec_id_foreign=spec1)

        spec2 = SpecGpu.objects.create(frequency_Mhz=2407, type_memory_str="GDDR7", memory_size_Gb=16)
        Gpu.objects.create(name="Nvidia RTX 5060 Ti", price=80000, spec_id_foreign=spec2)

        spec3 = SpecGpu.objects.create(frequency_Mhz=2325, type_memory_str="GDDR7", memory_size_Gb=12)
        Gpu.objects.create(name="Nvidia RTX 5070", price=90000, spec_id_foreign=spec3)

        spec4 = SpecGpu.objects.create(frequency_Mhz=2295, type_memory_str="GDDR7", memory_size_Gb=16)
        Gpu.objects.create(name="Nvidia RTX 5070 Ti", price=150000, spec_id_foreign=spec4)

        spec5 = SpecGpu.objects.create(frequency_Mhz=1875, type_memory_str="GDDR7", memory_size_Gb=16)
        Gpu.objects.create(name="Nvidia RTX 5080", price=240000, spec_id_foreign=spec5)

        spec6 = SpecGpu.objects.create(frequency_Mhz=2017, type_memory_str="GDDR7", memory_size_Gb=32)
        Gpu.objects.create(name="Nvidia RTX 5090", price=800000, spec=spec6)

