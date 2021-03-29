from django.urls import path
from Profile_app import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
      path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/', views.view_profile, name='view_profile'),
    # path('student/category/<int:pk>/', views.category_student_details, name='category_student_details'),
    path('member/', views.membership, name='membership'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('accoount/edit/', views.accoount_update, name='accoount_update'),
    # path('contact', views.contact, name='contact'),
    path('search', views.search_list, name='search_list'),
     path ('username-valid/', csrf_exempt(views.usernameValidation), name='username-valid'),
    path('email-validation/', csrf_exempt(views.emailValidation), name='email-validation'),
    path('login/', views.loginPage, name='login'),
]
