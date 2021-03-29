from django.urls import path
from About_app import views

urlpatterns = [
    path('about/<int:pk>/', views.about_category_details, name='about_detail')
]