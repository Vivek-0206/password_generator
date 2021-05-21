from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    pwd = []
    thepassword = ''
    length = int(request.GET.get('length'))

    characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    symbol = list('!@#$%*.')
    number = list('0123456789')

    if request.GET.get('special') and request.GET.get('number'):
        chlen = length//2
        splen = chlen//2
        nmlen = length - chlen - splen
        for x in range(chlen):
            pwd.append(random.choice(characters))
        for x in range(splen):
            pwd.append(random.choice(symbol))
        for x in range(nmlen):
            pwd.append(random.choice(number))
    elif request.GET.get('special'):
        chlen = length//2
        splen = length - chlen
        for x in range(chlen):
            pwd.append(random.choice(characters))
        for x in range(splen):
            pwd.append(random.choice(symbol))
    elif request.GET.get('number'):
        chlen = length//2
        nmlen = length - chlen
        for x in range(chlen):
            pwd.append(random.choice(characters))
        for x in range(nmlen):
            pwd.append(random.choice(number))
    else:
        for x in range(length):
            pwd.append(random.choice(characters))

    random.shuffle(pwd)

    for char in pwd:
        thepassword += char

    return render(request, 'generator/password.html', {'password': thepassword})
