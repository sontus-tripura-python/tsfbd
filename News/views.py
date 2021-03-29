from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from News.models import *
from Home_app.models import *
from News.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
import uuid
# Create your views here.

def news(request):
    news_list = News.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    lastes_news = News.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')[:5]
    paginator = Paginator(news_list, 4)
    page = request.GET.get('page')
    try:
        news_list = paginator.get_page(page)
    except PageNotAnInteger:
        news_list = paginator.get_page(1)
    except EmptyPage:
        news_list = paginator.get_page(paginator.num_pages)
    context = {'news_list': news_list,'lastes_news': lastes_news}
    return render(request, 'news_app/news_list.html', context )

def news_details(request, slug, pk):
    news = get_object_or_404(News, slug=slug, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if not request.user.is_authenticated:
                messages.info(request, 'Please login or Sign up to comment')
                return redirect('login')
            comment = form.save(commit=False)
            comment.user = request.user
            comment.news = news
            comment.save()
            return HttpResponseRedirect(reverse('news_details', kwargs={'slug': news.slug, 'pk': news.pk}))
        
    context = { 'news': news, 'form': form }
    return render(request, 'news_app/news_details.html', context)

@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_draft')
            
    else:
        form = NewsForm()
        context = {'form': form}
    return render(request, 'news_app/news_create.html', context)

@login_required
def news_draft(request):
    NewsDraft = News.objects.filter(publish_date__isnull=True).order_by('-created_date')
    context = {'NewsDraft': NewsDraft,}
    return render(request, 'news_app/news_draft.html',  context)

@login_required
def news_publish(request, slug, pk):
    news = get_object_or_404(News, slug=slug, pk=pk)
    news.publish()
    return redirect('news')
@login_required
def news_edit(request, slug, pk):
    news = get_object_or_404(News, slug=slug, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)

        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_details', news.pk)
    else:
        form = NewsForm(instance=news)
        stuff_for_frontend = {'form': form,}
    return render(request, 'news_app/news_create.html', stuff_for_frontend)

@login_required
def news_delete(request, slug, pk):
    news = get_object_or_404(News, slug=slug, pk=pk)
    news.delete()
    return redirect('news')