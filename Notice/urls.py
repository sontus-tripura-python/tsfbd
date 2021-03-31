from django.urls import path
from Notice import views

urlpatterns = [
    path('notice-create/', views.notice_create, name='notice_create')
]