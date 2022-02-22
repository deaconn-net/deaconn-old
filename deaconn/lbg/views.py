from django.shortcuts import render

def lbg_view(request):
    info = {}
    info["template_name"] = 'lbg/lbg.html'
    info["title"] = 'LBG - Deaconn'
    return render(request, 'home/page.html', info)