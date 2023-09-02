from django.shortcuts import render, redirect, reverse
from .myforms import RegForm


def index(req):
    return render(req, 'index.html')


def regform(req):
    if req.POST:
        data = req.POST.dict()
        data.pop('csrfmiddlewaretoken')
        try:
            avatar = req.FILES['avatar']
            file = open('anketa/static/upload/' + avatar.name, 'wb')
            file.write(avatar.read())
            file.close()
            data['avatar'] = '/upload/' + avatar.name
        except:
            pass
        return render(req, 'page.html', context=data)
    else:
        form = RegForm()
        return render(req, 'forma.html', context={'form': form})

