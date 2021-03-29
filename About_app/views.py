from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from About_app.models import *
from Home_app.models import *
# Create your views here.
def about_category_details(request, pk):
     categories = Category.objects.get( pk=pk)
     categories_details = About.objects.filter(category=categories)
     context = {'categories_details': categories_details,}
     return render(request, 'about_app/about.html', context)