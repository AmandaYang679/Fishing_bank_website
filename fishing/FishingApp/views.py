from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def homepage(request):
    return render(request, 'FishingApp/index.html')

def authorization(request):
    return render(request, 'FishingApp/auth.html')

def login(request):
    if request.method == 'POST':
        print(request.POST['login'] + '\n' + request.POST['password'])
        return HttpResponse('Вы попались!<br>' +
                            'Ваш логин: ' + request.POST['login'] +
                            '<br>Ваш пароль: ' + request.POST['password'])
    return redirect('')