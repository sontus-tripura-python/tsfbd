from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Home_app.models import *
from Notice.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
import uuid

@login_required
def notice_create(request):
    if request.method == 'POST':
        form = NoticeBoardForm(request.POST)
        if form.is_valid():
            news.save()
            return redirect('notice_draft')
            
    else:
        form = NoticeBoardForm()
        context = {'form': form}
    return render(request, 'Notice/notice_create.html', context)

@login_required
def news_draft(request):
    Notice_drafts = NoticeBoard.objects.filter(publish_date__isnull=True).order_by('-created_date')
    context = {'Notice_drafts': Notice_drafts,}
    return render(request, 'Notice/Notice_drafts.html',  context)

@login_required
def notice_publish(request, slug, pk):
    notice_publish = get_object_or_404(News, slug=slug, pk=pk)
    notice_publish.publish()
    return redirect('news')
@login_required
def notice_edit(request, slug, pk):
    notice = get_object_or_404(NoticeBoard, slug=slug, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=notice)
        if form.is_valid():
            news.save()
            return redirect('notice_details', notice.slug, notice.pk)
    else:
        form = NewsForm(instance=news)
        stuff_for_frontend = {'form': form,}
    return render(request, 'Notice/news_create.html', stuff_for_frontend)

@login_required
def Notice_delete(request, slug, pk):
    notice = get_object_or_404(NoticeBoard, slug=slug, pk=pk)
    notice.delete()
    return redirect('notice_list')

