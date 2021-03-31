from Notice.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def notice_list(request):
    notice_list = NoticeBoard.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    paginator = Paginator(notice_list, 2)
    page = request.GET.get('page')
    try:
        notice_list = paginator.get_page(page)
    except PageNotAnInteger:
        notice_list = paginator.get_page(1)
    except EmptyPage:
        notice_list = paginator.get_page(paginator.num_pages)
    
    return {'notice_list': notice_list }

@login_required
def news_draft(request):
    Notice_drafts = NoticeBoard.objects.filter(publish_date__isnull=True).order_by('-created_date')
    return {'news_draft': news_draft}