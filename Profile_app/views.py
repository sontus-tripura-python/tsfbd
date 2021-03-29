from django.shortcuts import render, redirect, get_object_or_404
from Profile_app.forms import *
from Profile_app.models import *
from Home_app.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
import json
from validate_email import validate_email
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def usernameValidation(request):
    data = json.loads(request.body)
    username = data['username']
    if not str(username).isalnum():
        return JsonResponse({'username_error': 'Username should only alphanumeric characters'}, status=200)
    if User.objects.filter(username=username).exists():
        return JsonResponse({'username_error': 'Username is already taken,choose another one'}, status=400)
    return JsonResponse({'username_valid': True})

def emailValidation(request):
    data = json.loads(request.body)
    email = data['email']
    if not validate_email(email):
        return JsonResponse({'email_error': 'Email is invalid, set your correct email address'}, status=400)
    if User.objects.filter(email=email):
        return JsonResponse({'email_error': 'Sorry, email address is already used, try another one'}, status=400)
    return JsonResponse("email validatioon", safe=False)



# def register(request):
#     about_inform = TsfAboutSetting.objects.get(id=1)
#     if request.user.is_authenticated:
#         return redirect('profile')
#     else:
#         if request.method == 'POST':
#             username = request.POST['username']
#             fname = request.POST['fname']
#             lname = request.POST['lname']
#             email = request.POST['email']
#             password = request.POST['password']
#             context = {'fieldValue': request.POST}
#             if not User.objects.filter(username=username).exists():
#                 if not User.objects.filter(email=email).exists():
#                     if len(password)<8:
#                         messages.error(request, 'password too short,it have to be minimun 8 characters')
#                         return render(request, 'account/register.html', context)
#                     if len(username)<5:
#                         messages.error(request, 'your username less than 5 characters, try again')
#                         return render(request, 'account/register.html', context)
#                     user = User.objects.create_user(username=username, email=email)
#                     user.first_name = fname
#                     user.last_name = lname
#                     user.set_password(password)
#                     user.save()
#                     messages.success(request, 'your account has been successfully created')
#                     return redirect('login')
        
#         return render(request, 'Profile_app/register.html', context={'about_inform': about_inform})


                   
def register(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            password = request.POST['password']
            context = {'fieldValue': request.POST}
            if not User.objects.filter(username=username).exists():
                if len(password)<8:
                    messages.error(request, 'password too short,it have to be minimun 8 characters')
                    return render(request, 'account/register.html', context)
                if len(username)<5:
                    messages.error(request, 'your username less than 5 characters, try again')
                    return render(request, 'account/register.html', context)
                user = User.objects.create_user(username=username)
                user.first_name = fname
                user.last_name = lname
                user.set_password(password)
                user.save()
                messages.success(request, 'your account has been successfully created')
                return redirect('login')
    
        return render(request, 'Profile_app/register.html', context={'about_inform': about_inform})


def loginPage(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.info(request, 'Username Or Passsword is incorrect')

    context = {'about_inform': about_inform}
    return render(request, 'Profile_app/login.html', context)

@login_required
def logout(request):
    return redirect('/')

def profile(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    return render(request, 'Profile_app/profile.html', context={'about_inform': about_inform })

def membership(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    users = User.objects.all()
    profile = Profile.objects.all()
    profile_count = profile.count()
    context = { 'users': users, 'profile_count': profile_count, 'about_inform': about_inform }

    return render(request, 'Profile_app/membership.html', context)

def view_profile(request, pk=None):
    about_inform = TsfAboutSetting.objects.get(id=1)
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    arg = {'user': user, 'about_inform': about_inform }
    return render(request, 'Profile_app/profile_views.html', arg)

def search_list(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    query = request.GET['query']
    allquery = Profile.objects.filter(
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)|
                Q(district__icontains=query)|
                Q(current_enroll__icontains=query)|
                Q(university__icontains=query)|
                Q(college__icontains=query)|
                Q(School__icontains=query)|
                Q(deparment__icontains=query)|
                Q(religion__icontains=query)|
                Q(Village__icontains=query)|
                Q(thana__icontains=query)|
                Q(Class__icontains=query)
        )
    return render(request, 'Profile_app/search.html', {'allquery': allquery })

@login_required
def edit_profile(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'p_form': p_form, 'about_inform': about_inform }
    return render (request, 'Profile_app/Profile_edit.html', context )

@login_required
def accoount_update(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {'u_form': u_form, 'about_inform': about_inform }
    return render (request, 'Profile_app/account_edit.html', context )






    