from django.shortcuts import render
from .myforms import *

datanames = ['E-mail:', 'Имя', 'Фамилия', 'Отчество', 'Пол:', 'Возраст', 'Язык',
             'Люблю собак?', 'Люблю кошек?', 'Умею готовить?', 'Религия:']


def index(req):
    return render(req, 'index.html')


def regform(req):
    if req.POST:
        form = RegForm(req.POST)
        data = list(req.POST.values())
        print(data)
    else:
        form = RegForm()
    return render(req, 'forma.html', context={'form': form})


def page(req):
    pass
