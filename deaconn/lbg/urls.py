from django.urls import path

from .views import lbg_view

app_name = 'lbg'
urlpatterns = [
    path('', lbg_view, name = 'index')
]