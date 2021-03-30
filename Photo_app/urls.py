from django.urls import path
from Photo_app import views

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('photo-details/<str:pk>/', views.gallery, name='gallery_with_pk'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
]