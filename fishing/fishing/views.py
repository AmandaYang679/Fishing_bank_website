from django.shortcuts import render


def homepage(request):
    return render(request, 'FishingApp/index.html')

def authorization(request):
    return render(request, 'FishingApp/auth.html')