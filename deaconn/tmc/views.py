from django.shortcuts import render

def tmc_view(request):
    info = {}
    info["template_name"] = 'tmc/tmc.html'
    info["title"] = 'TMC - Deaconn'
    return render(request, 'home/page.html', info)