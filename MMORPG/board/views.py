from django.shortcuts import render
import logging

# Create your views here.
def index(request):
    context = {'title':'Главная страница'}
    return render(request, 'board/add_new_post.html', context)