from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from .form import ConatactUsF


def MainView(request):
    ab = About_Md.objects.all()
    ft = Furnitures.objects.all()
    ts = Testimonial.objects.all()
    cu = ConatactUs.objects.all()
    form = ConatactUsF()

    if request.method == 'POST':
        form = ConatactUsF(request.POST)
        if form.is_valid():
            form.save()

    print(cu)
    print(ts)
    print(ab)
    context = {
        'form': form,
        'About': ab,
        'Ft': ft,
        'Ts': ts,
        'Cu': cu
    }

    return render(request, 'main/index.html', context)


def AboutView(request):
    about = About_Md.objects.all()
    form = ConatactUsF()

    if request.method == 'POST':
        form = ConatactUsF(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'about': about,
        'form': form,
    }

    return render(request, 'main/about.html', context)


def FurnituresView(request):
    ft = Furnitures.objects.all()
    form = ConatactUsF()

    if request.method == 'POST':
        form = ConatactUsF(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'ft': ft,
        'form': form
    }

    return render(request, 'main/furnitures.html', context)


def TestimonialsView(reqeust):
    ts = Testimonial.objects.all()
    form = ConatactUsF()

    if reqeust.method == 'POST':
        form = ConatactUsF(reqeust.POST)
        if form.is_valid():
            form.save()

    context = {
        'ts': ts,
        'form': form,
    }
    return render(reqeust, 'main/testimonial.html', context)


def ContextView(request):
    ct = ConatactUs.objects.all()
    form = ConatactUsF()

    if request.method == 'POST':
        form = ConatactUsF(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'ct': ct,
        'form': form
    }
    return render(request, 'main/contact.html', context)
