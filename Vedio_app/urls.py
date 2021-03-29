from django.urls import path
from Vedio_app import views
urlpatterns = [
    path('vedio-list/', views.vedio_list, name='vedio_list'),
    path('tag/<slug:tag_slug>/', views.vedio_list, name='vedio_list_by_tag'),
    path('vedio-play/<slug:slug>/', views.vedio_details, name='vedio_details'),
    path('audio-list/', views.audio_list, name='audio_list'),
]