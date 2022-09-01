from django.urls import path

from .views import tmc_view

app_name = 'tmc'
urlpatterns = [
    path('', tmc_view, name = 'index')
]