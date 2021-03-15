from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm, CategoryForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import BookFilter

# Create your views here.

def news_list(request):
    news = News.objects.all().order_by('-publish_at')


    myfilter = BookFilter(request.GET,queryset=news)
    news = myfilter.qs

    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'news':page_obj,
        'myfilter':myfilter,
    }
    return render(request, 'news_list.html', context)

def news_detail(request, slug):
    news = News.objects.get(slug=slug)
    context = {
        'news': news,
    }
    return render(request,'news_detail.html', context)
    

@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.save()
            form = NewsForm()
    else:
        form = NewsForm()

    return render(request,'add_news.html',{'form':form})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.save()
            form = CategoryForm()
    else:
        form = CategoryForm()
        
    return render(request,'add_category.html',{'form':form})
