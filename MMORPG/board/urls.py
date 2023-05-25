from django.urls import path
from .views import add_article, index, article_detail
app_name = 'board'
urlpatterns = [
    path('', index, name = 'index'),
    path('category/<int:category_id>/', index, name='category'),
    path('article/add/', add_article, name='add_article'),
    path('article/<int:article_id>/', article_detail, name = 'article_detail'),
]