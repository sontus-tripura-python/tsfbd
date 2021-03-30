"""tsfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from Profile_app import views as user_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = 'TSF.BD Admin Panel'
admin.site.site_title = 'TRIPURA STUEDNTS FORUM'
admin.site.index_title  = 'TRIPURA STUEDNTS FORUM ADMIN'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home_app.urls')),
    path('', include('News.urls')),
    path('', include('Profile_app.urls')),
    path('', include('Vedio_app.urls')),
    path('', include('Contact_app.urls')),
    path('', include('About_app.urls')),
    path('', include('CommitteApp.urls')),
    path('', include('Photo_app.urls')),
    path('', include('Notice.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    # third part link
    path('register/', user_views.register, name='register'),
    # path('login/',auth_views.LoginView.as_view(template_name='Profile_app/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='Profile_app/logout.html'), name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='Profile_app/password_reset.html'),
              name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='Profile_app/password_reset_done.html'),
             name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='Profile_app/password_reset_confirm.html'),
                 name='password_reset_confirm'),
   path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='Profile_app/password_reset_complete.html'),
                name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)