from django.shortcuts import render

def products_view(request):
    info = {}
    return render(request, 'products/products.html', info)