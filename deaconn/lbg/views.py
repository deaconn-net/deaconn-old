from django.shortcuts import render

def lbg_view(request):
    info = {}
    return render(request, 'lbg/lbg.html', info)