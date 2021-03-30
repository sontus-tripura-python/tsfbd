from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# # Create your views here.
def notice_list(request):
    return render(request, 'Notice/notice_list.html')
