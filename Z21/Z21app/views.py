from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import GPU


def index(request):
    gpus = GPU.objects.all()
    return render(request, "gpu.html", {"gpus": gpus})


def create(request):
    if request.method == "POST":
        gpus = GPU()
        gpus.brand = request.POST.get("brand")
        gpus.model = request.POST.get("model")
        gpus.video_memory_GB = request.POST.get("video_memory_GB")
        gpus.video_memory_type = request.POST.get("video_memory_type")
        gpus.save()
    return HttpResponseRedirect("/")
    # return render(request, "gpu.html", context=)


def edit(request, id):
    try:
        gpus = GPU.objects.get(id=id)
        if request.method == "POST":
            gpus.brand = request.POST.get("brand")
            gpus.model = request.POST.get("model")
            gpus.video_memory_GB = request.POST.get("video_memory_GB")
            gpus.video_memory_type = request.POST.get("video_memory_type")
            gpus.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "create.html", {"gpus": gpus})

    except GPU.DoesNotExist:
        return HttpResponseNotFound("<h2> Клиент не найден</h2>")


def delete(request, id):
    try:
        person=GPU.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except GPU.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")