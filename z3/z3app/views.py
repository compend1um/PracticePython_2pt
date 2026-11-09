from django.shortcuts import render

def homepage(request):
    return render(request, "homepage.html")

def customers(request):
    return render(request, "customers.html")

def sales_progress(request):
    return render(request, "sales_progress.html")

def products(request):
    return render(request, "products.html")

def sale(request):
    return render(request, "sale.html")
