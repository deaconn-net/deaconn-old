from django.urls import path

from .views import speedruntg_view

app_name = 'speedruntg'
urlpatterns = [
    path('', speedruntg_view, name = 'index')
]