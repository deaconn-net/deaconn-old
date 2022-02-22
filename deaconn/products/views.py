from django.shortcuts import render

def products_view(request):
    info = {}
    info["template_name"] = 'products/products.html'
    info["title"] = 'Products - Deaconn'
    return render(request, 'home/page.html', info)