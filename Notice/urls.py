from django.urls import path
from Notice import views

urlpatterns = [
    path('Notice/', views.notice_list, name='notice_list')
]