from django.shortcuts import render


def home(request):
    return render(request, 'portal/home.html')


def register(request):
    return render(request, 'portal/register.html')
