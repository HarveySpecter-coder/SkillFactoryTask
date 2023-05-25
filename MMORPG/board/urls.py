from django.urls import path, include
from .views import add_article, index
app_name = 'board'
urlpatterns = [
    path('', index, name = 'index'),
    path('article/add/', add_article, name='add_article'),
]