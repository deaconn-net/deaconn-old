from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_view, name = 'index'),
    path('<int:article_id>-<slug:slug>/', views.article_view, name = 'article'),
    path('create_article/', views.create_article, name = 'create_article')
]