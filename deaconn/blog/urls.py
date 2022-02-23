from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_view, name = 'index'),
    path('<int:article_id>/', views.article_view, name = 'article')
]