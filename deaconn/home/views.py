from django.shortcuts import render

def home_view(request):
    info = {}
    return render(request, 'home/home.html', info)