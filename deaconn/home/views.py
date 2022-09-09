import markdown

from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from video_markdown import VideoExtension

def home_view(request):
    info = {}
    info["gh_stars"] = 243
    info["gh_repos"] = 99
    info["gh_followers"] = 2302
    info["gh_commits"] = 5034
    info["template_name"] = 'home/home.html'
    info["title"] = 'Home - Deaconn'
    return render(request, 'home/page.html', info)

@csrf_exempt
def convert_with_markdown(request):
    contents = None

    if 'contents' in request.POST:
        contents = request.POST["contents"]

    if contents is None:
        return HttpResponse("404")
    else:
        return HttpResponse(markdown.markdown(contents, extensions=['fenced_code', 'codehilite']))