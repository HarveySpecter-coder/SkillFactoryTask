from django.shortcuts import render, HttpResponseRedirect
from .forms import ArticleForm
from .models import Article, Category
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('board:index'))
    else:
        form = ArticleForm()
    context = {'title':'Добавить статью', 'form':form}
    return render(request, 'board/add_new_post.html', context)

def index(request, category_id=None):
    if category_id:
        current_category = Category.objects.get(id=category_id)
        articles = Article.objects.filter(category=current_category)
    else:
        articles = Article.objects.all()
    categories = Category.objects.all()
    context = {'articles':articles, 'categories':categories}
    return render(request, 'board/index.html', context)

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article':article}
    return render(request, 'board/article_detail.html', context)