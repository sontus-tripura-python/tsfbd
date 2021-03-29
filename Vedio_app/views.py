from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from Home_app.models import *
from About_app.models import *
from Vedio_app.models import *
from taggit.models import Tag
from django.db.models import Count
from Vedio_app.forms import *
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def vedio_list(request, tag_slug=None):
    about_categories = Category.objects.all()
    about_inform = TsfAboutSetting.objects.get(id=1)
    vedio_lists = Vedio.objects.all()
    paginator = Paginator(vedio_lists, 4)
    page = request.GET.get('page')
    try:
        vedio_lists = paginator.get_page(page)
    except PageNotAnInteger:
        vedio_lists = paginator.get_page(1)
    except EmptyPage:
        vedio_lists = paginator.get_page(paginator.num_pages)
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        vedio_lists = vedio_lists.filter(tags__in=[tag])
    context={'about_inform': about_inform, 'vedio_lists': vedio_lists, 
           'about_categories': about_categories, 'tag': tag }
    return render(request, 'vedio_app/vedio_list.html', context)

def vedio_details(request, slug):
    about_categories = Category.objects.all()
    about_inform = TsfAboutSetting.objects.get(id=1)
    video = get_object_or_404(Vedio, slug=slug)
    video_tags = video.tags.values_list('id', flat=True)
    similiar_vedio = Vedio.objects.filter(tags__in=video_tags).exclude(id=video.id)
    similiar_vedio = similiar_vedio.annotate(same_tags=Count('tags')).order_by('-same_tags')[:4]
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.vedio = video
            form.save()
            return HttpResponseRedirect(reverse('vedio_details', args=(video.slug,)))
    context = {'video': video, 'about_categories': about_categories, 
      'about_inform': about_inform, 'similiar_vedio': similiar_vedio, 'form': form }
    return render(request, 'vedio_app/video_details.html', context)




def audio_list(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    context = {'about_inform': about_inform }
    return render(request, 'audio/audio.html', context)