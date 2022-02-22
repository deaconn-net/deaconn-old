from django.shortcuts import render

def home_view(request):
    info = {}
    info["gh_stars"] = 243
    info["gh_repos"] = 99
    info["gh_followers"] = 2302
    info["gh_commits"] = 5034
    info["template_name"] = 'home/home.html'
    info["title"] = 'Home - Deaconn'
    return render(request, 'home/page.html', info)