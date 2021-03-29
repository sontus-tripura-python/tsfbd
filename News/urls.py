from django.urls import path

from News import views

urlpatterns = [
      path('news/', views.news, name='news'),
    path('news-detail/<slug:slug>/<int:pk>/', views.news_details, name='news_details'),
    path('create/', views.news_create, name='news_create'),
     path('news/draft/', views.news_draft, name='news_draft'),
     path('news-publish/<slug:slug>/<int:pk>/', views.news_publish, name='news_publish'),
     path('news-edit/<slug:slug>/<int:pk>/', views.news_edit, name='news_edit'),
     path('news-delete/<slug:slug>/<int:pk>/', views.news_delete, name='news_delete'),
]