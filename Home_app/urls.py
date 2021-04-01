from django.urls import path
from Home_app import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('students/<int:pk>/', views.studentscategory, name='studentscategory'),
    path('member/student-search/', csrf_exempt(views.search_students), name='search_students'),
    path('student-seach/', views.search_list_student, name='search_list_student'),

]
