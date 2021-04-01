from Notice.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def notice_list(request):
    notice_list = NoticeBoard.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')[:1]
    return {'notice_list': notice_list }
