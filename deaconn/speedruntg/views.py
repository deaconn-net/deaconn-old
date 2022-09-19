from django.shortcuts import render

def speedruntg_view(request):
    info = {}
    info["template_name"] = 'speedruntg/speedruntg.html'
    info["title"] = 'Speedrun: The Game - Deaconn'
    return render(request, 'home/page.html', info)